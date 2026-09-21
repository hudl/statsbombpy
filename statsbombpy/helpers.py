from collections import defaultdict

import pandas as pd

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


def is_relevant(event, filters):
    return all(event.get("type", {}).get("name") == v for k, v in filters.items())


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
