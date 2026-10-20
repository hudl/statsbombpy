import warnings

import requests as req

import statsbombpy.entities as ents
from statsbombpy.cache import session
from statsbombpy.config import API_VERSION_KEYS, HOSTNAME, VERSIONS, _VERSION

HEADERS = {"User-Agent": f"statsbombpy/{_VERSION}"}

# session-lifetime cache; None until the first successful fetch
_ENDPOINT_VERSIONS = None


class NoAuthWarning(UserWarning):
    """Warning raised when no user credentials are provided."""

    pass


def has_auth(creds):
    if creds.get("user") in [None, ""] or creds.get("passwd") in [None, ""]:
        warnings.warn(
            "credentials were not supplied. open data access only", NoAuthWarning
        )
        return False
    return True


def get_resource(url: str, creds: dict) -> list:
    auth = req.auth.HTTPBasicAuth(creds["user"], creds["passwd"])
    resp = session.get(url, auth=auth, headers=HEADERS)
    if resp.status_code >= 500:
        # transient server error: don't mistake it for an empty result
        resp.raise_for_status()
    if resp.status_code != 200:
        print(f"{url} -> {resp.status_code}")
        resp = []
    else:
        resp = resp.json()
    return resp


def _fetch_endpoint_versions(creds: dict):
    try:
        raw = get_resource(f"{HOSTNAME}/api/endpoint-versions", creds)
    except req.HTTPError:
        return None
    if not raw:
        return None
    return {
        API_VERSION_KEYS[k]: f"v{v}"
        for k, v in raw.items()
        if k in API_VERSION_KEYS
    }


def endpoint_versions(creds: dict) -> dict:
    """Return the live endpoint-versions map, fetched once per session.

    Falls back to the hardcoded VERSIONS until a fetch succeeds, so a failed
    or unauthenticated request never caches a bad value.
    """
    global _ENDPOINT_VERSIONS
    if _ENDPOINT_VERSIONS is None:
        _ENDPOINT_VERSIONS = _fetch_endpoint_versions(creds)
    return _ENDPOINT_VERSIONS or VERSIONS


def _normalize_version(version) -> str:
    version = str(version)
    return version if version.startswith("v") else f"v{version}"


def resolve_version(endpoint: str, creds: dict, version=None) -> str:
    """Resolve the API version for an endpoint.

    A caller-supplied version wins (accepts "v9", 9 or "9"); otherwise the
    live endpoint-versions map is used, falling back to VERSIONS.
    """
    if version is not None:
        return _normalize_version(version)
    return endpoint_versions(creds).get(endpoint, VERSIONS[endpoint])


def competitions(creds: dict, version: str = None) -> dict:
    v = resolve_version("competitions", creds, version)
    url = f"{HOSTNAME}/api/{v}/competitions"
    competitions = get_resource(url, creds)
    return ents.competitions(competitions)


def matches(
    competition_id: int, season_id: int, creds: dict, version: str = None
) -> dict:
    v = resolve_version("matches", creds, version)
    url = (
        f"{HOSTNAME}/api/{v}/competitions/{competition_id}"
        f"/seasons/{season_id}/matches"
    )
    matches = get_resource(url, creds)
    return ents.matches(matches)


def lineups(match_id: int, creds: dict, version: str = None) -> dict:
    v = resolve_version("lineups", creds, version)
    url = f"{HOSTNAME}/api/{v}/lineups/{match_id}"
    lineups = get_resource(url, creds)
    return ents.lineups(lineups)


def events(match_id: int, creds: dict, version: str = None) -> dict:
    v = resolve_version("events", creds, version)
    url = f"{HOSTNAME}/api/{v}/events/{match_id}"
    events = get_resource(url, creds)
    return ents.events(events, match_id)


def frames(match_id: int, creds: dict, version: str = None) -> list:
    v = resolve_version("360-frames", creds, version)
    url = f"{HOSTNAME}/api/{v}/360-frames/{match_id}"
    frames = get_resource(url, creds)
    return ents.frames(frames, match_id)


def player_match_stats(
    match_id: int, creds: dict, version: str = None
) -> list:
    v = resolve_version("player-match-stats", creds, version)
    url = f"{HOSTNAME}/api/{v}/matches/{match_id}/player-stats"
    return get_resource(url, creds)


def player_season_stats(
    competition_id: int, season_id: int, creds: dict, version: str = None
) -> list:
    v = resolve_version("player-season-stats", creds, version)
    url = (
        f"{HOSTNAME}/api/{v}/competitions/{competition_id}"
        f"/seasons/{season_id}/player-stats"
    )
    return get_resource(url, creds)


def team_match_stats(
    match_id: int, creds: dict, version: str = None
) -> list:
    v = resolve_version("team-match-stats", creds, version)
    url = f"{HOSTNAME}/api/{v}/matches/{match_id}/team-stats"
    return get_resource(url, creds)


def team_season_stats(
    competition_id: int, season_id: int, creds: dict, version: str = None
) -> list:
    v = resolve_version("team-season-stats", creds, version)
    url = (
        f"{HOSTNAME}/api/{v}/competitions/{competition_id}"
        f"/seasons/{season_id}/team-stats"
    )
    return get_resource(url, creds)
