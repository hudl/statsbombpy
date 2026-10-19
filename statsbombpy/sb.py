from functools import partial
from multiprocessing import Pool
from typing import Union

import pandas as pd

from statsbombpy import api_client, public
from statsbombpy.config import DEFAULT_CREDS, MAX_CONCURRENCY
from statsbombpy.helpers import (filter_and_group_events,
                                 merge_events_and_frames, reduce_events,
                                 split_location_cols)


def competitions(fmt="dataframe", creds: dict = DEFAULT_CREDS, version: str = None):
    if api_client.has_auth(creds) is True:
        competitions = api_client.competitions(creds, version=version)
    else:
        competitions = public.competitions()
    if fmt == "dataframe":
        if isinstance(competitions, dict):
            competitions = competitions.values()
        competitions = pd.DataFrame(competitions)
    return competitions


def matches(
    competition_id: int,
    season_id: int,
    fmt="dataframe",
    creds: dict = DEFAULT_CREDS,
    version: str = None,
):
    if api_client.has_auth(creds) is True:
        matches = api_client.matches(
            competition_id, season_id, creds=creds, version=version
        )
    else:
        matches = public.matches(competition_id, season_id)
    if fmt == "dataframe":
        home_managers = [
            (
                ", ".join(
                    [m["name"] for m in matches[match]["home_team"]["managers"]]
                    if "managers" in matches[match]["home_team"]
                    else ""
                )
            )
            for match in matches
        ]
        away_managers = [
            (
                ", ".join(
                    [m["name"] for m in matches[match]["away_team"]["managers"]]
                    if "managers" in matches[match]["away_team"]
                    else ""
                )
            )
            for match in matches
        ]

        def _extract_manager_cols(matches_dict, team_key):
            prefix = "home_manager" if team_key == "home_team" else "away_manager"
            rows = []
            for match in matches_dict.values():
                managers = match.get(team_key, {}).get("managers", [])
                if managers:
                    normalized = pd.json_normalize(managers, sep="_")
                    if len(normalized) > 1:
                        row = {
                            col: ", ".join(normalized[col].dropna().astype(str).tolist())
                            for col in normalized.columns
                        }
                    else:
                        row = normalized.iloc[0].to_dict()
                else:
                    row = {}
                rows.append(row)
            return pd.DataFrame(rows).add_prefix(f"{prefix}_")

        home_manager_df = _extract_manager_cols(matches, "home_team")
        away_manager_df = _extract_manager_cols(matches, "away_team")

        matches = pd.DataFrame(matches.values())

        def _normalize_with_prefix(series, prefix):
            df = pd.json_normalize(series.tolist(), sep="_").add_prefix(f"{prefix}_")
            double = f"{prefix}_{prefix}_"
            df.columns = [c.replace(double, f"{prefix}_", 1) if c.startswith(double) else c for c in df.columns]
            return df

        comp_df = _normalize_with_prefix(matches["competition"], "competition")
        comp_df["competition"] = comp_df["competition_country_name"] + " - " + comp_df["competition_name"]
        matches = matches.drop(columns=["competition"]).join(comp_df)

        season_df = _normalize_with_prefix(matches["season"], "season").rename(columns={"season_name": "season"})
        matches = matches.drop(columns=["season"]).join(season_df)

        for col in ["home_team", "away_team"]:
            team_series = matches[col].apply(lambda t: {k: v for k, v in t.items() if k != "managers"})
            team_df = _normalize_with_prefix(team_series, col).rename(columns={f"{col}_name": col})
            matches = matches.drop(columns=[col]).join(team_df)

        for col in ["competition_stage", "stadium", "referee"]:
            if col in matches.columns:
                col_series = matches[col].apply(lambda x: x if isinstance(x, dict) else {})
                expanded = _normalize_with_prefix(col_series, col).rename(columns={f"{col}_name": col})
                matches = matches.drop(columns=[col]).join(expanded)

        matches["home_managers"] = home_managers
        matches["away_managers"] = away_managers
        for col in home_manager_df.columns:
            matches[col] = home_manager_df[col].values
        for col in away_manager_df.columns:
            matches[col] = away_manager_df[col].values
        metadata = matches.pop("metadata")
        for k in ["data_version", "shot_fidelity_version", "xy_fidelity_version"]:
            matches[k] = metadata.apply(lambda x: x.get(k))
    return matches


def lineups(
    match_id, fmt="dataframe", creds: dict = DEFAULT_CREDS, version: str = None
):
    if api_client.has_auth(creds) is True:
        lineups = api_client.lineups(match_id, creds=creds, version=version)
    else:
        lineups = public.lineups(match_id)
    if fmt == "dataframe":
        lineups_ = {}
        for lineup in lineups.values():

            lineup_ = pd.DataFrame(lineup["lineup"])
            lineup_["country"] = lineup_.country.apply(
                        lambda c: c["name"] if isinstance(c, dict) else "Unknown"
                    )
            if "formations" in lineup:
                lineup_["formations"] = str(lineup["formations"])
            if "events" in lineup:
                lineup_["events"] = str(lineup["events"])

            lineups_[lineup["team_name"]] = lineup_

        lineups = lineups_
    return lineups


def events(
    match_id: int,
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    flatten_attrs: bool = True,
    creds: dict = DEFAULT_CREDS,
    include_360_metrics=False,
    version: str = None,
    split_locations: bool = False,
) -> Union[pd.DataFrame, dict]:

    if not api_client.has_auth(creds) and include_360_metrics:
        raise Exception("360 metrics not available in open data")
    if api_client.has_auth(creds) is True:
        events = api_client.events(match_id, creds=creds, version=version)
    else:
        events = public.events(match_id)

    if include_360_metrics:
        frames = _360_frames(match_id, creds=creds)
        events = merge_events_and_frames(events, frames)

    if fmt == "dataframe":
        events = filter_and_group_events(events, filters, fmt, flatten_attrs)
        for ev_type, evs in events.items():
            events[ev_type] = pd.DataFrame(evs)
            if split_locations:
                events[ev_type] = split_location_cols(events[ev_type])
        if split is False:
            events = pd.concat([*events.values()], axis=0, ignore_index=True, sort=True)
    return events


def competition_events(
    country: str,
    division: str,
    season: str,
    gender: str = "male",
    split: bool = False,
    filters: dict = {},
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    include_360_metrics=False,
    version: str = None,
) -> Union[pd.DataFrame, dict]:

    c = competitions(creds=creds, fmt="dict")[country, division, season, gender]

    events_call = partial(
        events,
        fmt="json",
        creds=creds,
        include_360_metrics=include_360_metrics,
        version=version,
    )
    with Pool(MAX_CONCURRENCY) as p:
        matches_events = p.map(
            events_call,
            matches(c["competition_id"], c["season_id"], fmt="dict", creds=creds),
        )
        matches_events = map(
            lambda events: filter_and_group_events(
                events, filters, fmt, fmt == "dataframe"
            ),
            matches_events,
        )

    competition_events = reduce_events(matches_events, fmt)
    if fmt == "dataframe" and split is False:
        competition_events = pd.concat(
            [*competition_events.values()], axis=0, ignore_index=True, sort=True
        )
    return competition_events


def _360_frames(
    match_id: int,
    creds: dict = DEFAULT_CREDS,
    version: str = None,
) -> Union[pd.DataFrame, list, dict]:
    if api_client.has_auth(creds) is True:
        frames = api_client.frames(match_id, creds=creds, version=version)
    else:
        frames = public.frames(match_id)
    return frames


def frames(
    match_id: int,
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    version: str = None,
) -> Union[pd.DataFrame, list, dict]:
    frames = _360_frames(match_id, creds, version=version)
    for frame in frames:
        if "distances_from_edge_of_visible_area" in frame:
            if frame["distances_from_edge_of_visible_area"] is not None:
                for ff, d_from_vis_area in zip(
                    frame["freeze_frame"], frame["distances_from_edge_of_visible_area"]
                ):
                    ff["distance_from_edge_of_visible_area"] = d_from_vis_area["distance"]
    keys = ["event_uuid", "visible_area", "match_id", "freeze_frame"]
    frames = [{key: frame[key] for key in keys} for frame in frames]
    if fmt == "dataframe":
        frames = pd.DataFrame(frames).explode("freeze_frame")
        frames = pd.concat(
            [
                frames.drop("freeze_frame", axis=1).reset_index(drop=True),
                pd.json_normalize(frames.freeze_frame).reset_index(drop=True),
            ],
            axis=1,
        )
        frames = frames.rename(columns={"event_uuid": "id"})
    return frames


def competition_frames(
    country: str,
    division: str,
    season: str,
    gender: str = "male",
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    version: str = None,
) -> Union[pd.DataFrame, dict]:

    c = competitions(creds=creds, fmt="dict")[country, division, season, gender]

    frames_call = partial(
        frames,
        fmt="json",
        creds=creds,
        version=version,
    )
    with Pool(MAX_CONCURRENCY) as p:
        competition_frames = p.map(
            frames_call,
            matches(c["competition_id"], c["season_id"], fmt="dict", creds=creds),
        )

    if fmt == "dataframe":
        competition_frames = pd.concat(
            [
                pd.json_normalize(
                    frame,
                    "freeze_frame",
                    ["event_uuid", "match_id", "visible_area"],
                )
                for frame in competition_frames
            ],
            axis=0,
            ignore_index=True,
            sort=True,
        )
    return competition_frames


def player_match_stats(
    match_id: int,
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    version: str = None,
) -> Union[pd.DataFrame, dict]:
    if api_client.has_auth(creds) is True:
        player_match_stats = api_client.player_match_stats(
            match_id, creds=creds, version=version
        )
    else:
        raise Exception(
            "There is currently no open data for aggregated stats, please provide credentials"
        )
    if fmt == "dataframe":
        player_match_stats = pd.json_normalize(player_match_stats)
    return player_match_stats


def player_season_stats(
    competition_id: int,
    season_id: int,
    fmt="dataframe",
    creds: dict = DEFAULT_CREDS,
    version: str = None,
) -> Union[pd.DataFrame, dict]:
    if api_client.has_auth(creds) is True:
        player_season_stats = api_client.player_season_stats(
            competition_id, season_id, creds=creds, version=version
        )
    else:
        raise Exception(
            "There is currently no open data for aggregated stats, please provide credentials"
        )
    if fmt == "dataframe":
        player_season_stats = pd.json_normalize(player_season_stats)
    return player_season_stats


def team_match_stats(
    match_id: int,
    fmt: str = "dataframe",
    creds: dict = DEFAULT_CREDS,
    version: str = None,
) -> Union[pd.DataFrame, dict]:
    if api_client.has_auth(creds) is True:
        team_match_stats = api_client.team_match_stats(
            match_id, creds=creds, version=version
        )
    else:
        raise Exception(
            "There is currently no open data for aggregated stats, please provide credentials"
        )
    if fmt == "dataframe":
        team_match_stats = pd.json_normalize(team_match_stats)
    return team_match_stats


def team_season_stats(
    competition_id: int,
    season_id: int,
    fmt="dataframe",
    creds: dict = DEFAULT_CREDS,
    version: str = None,
) -> Union[pd.DataFrame, dict]:
    if api_client.has_auth(creds) is True:
        team_season_stats = api_client.team_season_stats(
            competition_id, season_id, creds=creds, version=version
        )
    else:
        raise Exception(
            "There is currently no open data for aggregated stats, please provide credentials"
        )
    if fmt == "dataframe":
        team_season_stats = pd.json_normalize(team_season_stats)
    return team_season_stats
