from collections import defaultdict

import pandas as pd

LOCATION_COLUMNS = [
    "location",
    "pass_end_location",
    "carry_end_location",
    "shot_end_location",
    "goalkeeper_end_location",
]

PLURALS = {
    "Starting XI": "starting_xis",
    "Half Start": "half_starts",
    "Camera On": "camera ons",
    "Camera off": "camera offs",
    "Pass": "passes",
    "Ball Receipt*": "ball_receipts",
    "Carry": "carrys",
    "Pressure": "pressures",
    "Foul Committed": "foul_committeds",
    "Foul Won": "foul_wons",
    "Duel": "duels",
    "Interception": "interceptions",
    "Block": "blocks",
    "Referee Ball-Drop": "referee_ball_drops",
    "Ball Recovery": "ball_recoverys",
    "Dispossessed": "dispossesseds",
    "Clearance": "clearances",
    "Dribble": "dribbles",
    "Miscontrol": "miscontrols",
    "Shot": "shots",
    "Goal Keeper": "goal_keepers",
    "Dribbled Past": "dribbled_pasts",
    "Injury Stoppage": "injury_stoppages",
    "Half End": "half_ends",
    "Substitution": "substitutions",
    "Shield": "shields",
    "Tactical Shift": "tactical_shifts",
    "Own Goal Against": "own_goal_againsts",
    "Own Goal For": "own_goal_fors",
    "Bad Behaviour": "bad_behaviours",
    "Player Off": "player_offs",
    "Player On": "player_ons",
    "50/50": "50/50s",
    "Error": "errors",
    "Offside": "offsides",
}


def flatten_event(event, flatten_attrs):
    if flatten_attrs:
        ev_type = event["type"]["name"].lower().replace(" ", "_").replace("*", "")
        ev_type = ev_type.replace("/", "_")
        ev_type = ev_type if event["type"]["name"] != "Goal Keeper" else "goalkeeper"
        if ev_type in event:
            for k, v in event[ev_type].items():
                event[f"{ev_type}_{k}"] = v
            del event[ev_type]

    for k, v in event.copy().items():
        if isinstance(v, dict) and "name" in v:
            event[k] = v["name"]
            if k in [
                "possession_team",
                "player",
                "team",
                "pass_recipient",
                "substitution_outcome",
                "substitution_replacement",
            ]:
                event[f"{k}_id"] = v["id"]
    return event


def filter_and_group_events(events, filters, fmt, flatten_attrs):
    events_ = defaultdict(list)
    for ev in events.values():
        ev_type = PLURALS[ev["type"]["name"]]
        if not is_relevant(ev, filters):
            continue
        if fmt == "dataframe":
            ev = flatten_event(ev, flatten_attrs)
        events_[ev_type].append(ev)
    return events_


def _attr_value(event, key):
    # attributes like type/player/team are {"id", "name"} dicts; others are scalars
    value = event.get(key)
    return value.get("name") if isinstance(value, dict) else value


def is_relevant(event, filters):
    return all(_attr_value(event, k) == v for k, v in filters.items())


def reduce_events(all_events: dict, fmt: str) -> dict:
    reduced_events: dict = defaultdict(list)
    for events in all_events:
        for ev_type, evs in events.items():
            reduced_events[ev_type] = reduced_events.get(ev_type, []) + evs
    if fmt == "dataframe":
        for ev_type, evs in reduced_events.items():
            reduced_events[ev_type] = pd.DataFrame(evs)
    return reduced_events


def merge_events_and_frames(
    events: dict,
    frames: list,
    drop_keys=[
        "event_uuid",
        "visible_area",
        "freeze_frame",
        "visible_player_counts",
        "distances_from_edge_of_visible_area",
    ],
) -> dict:
    frames = {frame["event_uuid"]: frame for frame in frames}
    events = {k: {**v, **frames.get(k, {})} for k, v in events.items()}
    for _, event in events.items():
        for key in list(event):
            if key == "visible_player_counts":
                for team in event[key]:
                    if team["team_id"] == event["team"]["id"]:
                        event["visible_teammates"] = team["count"]
                    else:
                        event["visible_opponents"] = team["count"]
            if key in drop_keys:
                del event[key]
    return events


def split_location_cols(df: pd.DataFrame, location_columns=None) -> pd.DataFrame:
    """Split list-like coordinate columns into flat float columns.

    StatsBomb locations come through as Python lists (e.g. [x, y] or
    [x, y, z] for shots), which are awkward to work with downstream:
    they are unhashable (drop_duplicates fails), they block vectorised
    operations, and they do not round-trip cleanly through Parquet
    (lists come back as numpy arrays). This helper adds ``<col>_x``,
    ``<col>_y`` (and ``<col>_z`` where a third coordinate exists)
    columns next to each list-like location column.

    Missing or malformed values yield NaN. Original columns are kept.
    """
    if location_columns is None:
        location_columns = LOCATION_COLUMNS

    def _coord(value, i):
        if isinstance(value, (list, tuple)) and len(value) > i:
            return value[i]
        # numpy arrays appear when a dataframe has been cached to Parquet
        if hasattr(value, "__len__") and not isinstance(value, (str, dict)):
            try:
                return value[i] if len(value) > i else float("nan")
            except (TypeError, IndexError):
                return float("nan")
        return float("nan")

    for col in location_columns:
        if col not in df.columns:
            continue
        values = df[col]
        df[f"{col}_x"] = pd.to_numeric(values.map(lambda v: _coord(v, 0)), errors="coerce")
        df[f"{col}_y"] = pd.to_numeric(values.map(lambda v: _coord(v, 1)), errors="coerce")
        z = pd.to_numeric(values.map(lambda v: _coord(v, 2)), errors="coerce")
        if z.notna().any():
            df[f"{col}_z"] = z
    return df


def get_possession_sequence(
    events: pd.DataFrame, event_id: str, exclude_trigger: bool = True
) -> pd.DataFrame:
    """
    Return all events in the same possession sequence as the given event.

    Parameters
    ----------
    events : pd.DataFrame
        Events for a single match, as returned by ``sb.events()``.
    event_id : str
        The ``id`` of any event in the target possession sequence.
        Typically the goal or significant event that ended the sequence.
    exclude_trigger : bool
        When True (default), the event identified by ``event_id`` is
        excluded from the result. Useful for build-up analysis where the
        trigger (e.g. a goal) is the endpoint rather than part of the
        sequence itself.

    Returns
    -------
    pd.DataFrame
        Events sorted by (period, timestamp, index). Empty DataFrame if
        ``event_id`` is not found in ``events``.
    """
    trigger = events[events["id"] == event_id]
    if trigger.empty:
        return pd.DataFrame()
    possession_id = trigger.iloc[0]["possession"]
    sequence = events[events["possession"] == possession_id]
    if exclude_trigger:
        sequence = sequence[sequence["id"] != event_id]
    return sequence.sort_values(["period", "timestamp", "index"]).reset_index(drop=True)


def get_prior_possession(events: pd.DataFrame, event_id: str) -> pd.DataFrame:
    """
    Return all events in the possession sequence immediately before the
    given event's possession.

    Useful for set piece context: when a goal is scored from a penalty,
    free kick, or corner, the foul or challenge that earned the set piece
    belongs to the prior possession (``possession - 1``).

    Parameters
    ----------
    events : pd.DataFrame
        Events for a single match, as returned by ``sb.events()``.
    event_id : str
        The ``id`` of any event in the target possession sequence.

    Returns
    -------
    pd.DataFrame
        Events sorted by (period, timestamp, index). Empty DataFrame if
        ``event_id`` is not found or there is no prior possession.
    """
    trigger = events[events["id"] == event_id]
    if trigger.empty:
        return pd.DataFrame()
    possession_id = trigger.iloc[0]["possession"]
    if possession_id <= 1:
        return pd.DataFrame()
    prior = events[events["possession"] == possession_id - 1]
    return prior.sort_values(["period", "timestamp", "index"]).reset_index(drop=True)
