import pandas as pd

from statsbombpy.helpers import (
    get_possession_sequence,
    get_prior_possession,
    is_relevant,
)

EV = {
    "type": {"name": "Pass"},
    "player": {"name": "Lionel Messi"},
    "minute": 10,
}


def test_filter_on_type():
    assert is_relevant(EV, {"type": "Pass"})
    assert not is_relevant(EV, {"type": "Shot"})


def test_filter_uses_the_given_key():
    assert is_relevant(EV, {"player": "Lionel Messi"})
    assert not is_relevant(EV, {"player": "Pass"})


def test_filter_on_scalar_attribute():
    assert is_relevant(EV, {"minute": 10})
    assert not is_relevant(EV, {"minute": 11})


def test_filter_on_missing_attribute_does_not_match():
    assert not is_relevant(EV, {"team": "Barcelona"})


def test_multiple_filters_are_anded():
    assert is_relevant(EV, {"type": "Pass", "player": "Lionel Messi"})
    assert not is_relevant(EV, {"type": "Shot", "player": "Lionel Messi"})


def test_no_filters_matches_everything():
    assert is_relevant(EV, {})


# Synthetic match events, deliberately shuffled. "e3" and "e4" share a
# timestamp so only the ``index`` column can order them.
EVENTS = pd.DataFrame(
    [
        {"id": "e5", "index": 5, "period": 1, "timestamp": "00:00:09.000", "possession": 2},
        {"id": "e4", "index": 4, "period": 1, "timestamp": "00:00:07.000", "possession": 2},
        {"id": "e1", "index": 1, "period": 1, "timestamp": "00:00:00.000", "possession": 1},
        {"id": "e3", "index": 3, "period": 1, "timestamp": "00:00:07.000", "possession": 2},
        {"id": "e2", "index": 2, "period": 1, "timestamp": "00:00:03.000", "possession": 1},
        {"id": "e7", "index": 7, "period": 2, "timestamp": "00:00:00.000", "possession": 3},
        {"id": "e6", "index": 6, "period": 1, "timestamp": "00:45:01.000", "possession": 2},
    ]
)


def test_possession_sequence_excludes_trigger_by_default():
    seq = get_possession_sequence(EVENTS, "e5")
    assert list(seq["id"]) == ["e3", "e4", "e6"]


def test_possession_sequence_includes_trigger_when_requested():
    seq = get_possession_sequence(EVENTS, "e5", exclude_trigger=False)
    assert list(seq["id"]) == ["e3", "e4", "e5", "e6"]


def test_possession_sequence_breaks_timestamp_ties_by_index():
    seq = get_possession_sequence(EVENTS, "e6", exclude_trigger=False)
    assert list(seq["id"][:2]) == ["e3", "e4"]


def test_possession_sequence_sorts_by_period_first():
    seq = get_possession_sequence(EVENTS.assign(possession=1), "e7", exclude_trigger=False)
    assert list(seq["id"]) == ["e1", "e2", "e3", "e4", "e5", "e6", "e7"]


def test_possession_sequence_unknown_event_id():
    seq = get_possession_sequence(EVENTS, "not-a-real-id")
    assert isinstance(seq, pd.DataFrame)
    assert seq.empty


def test_prior_possession():
    prior = get_prior_possession(EVENTS, "e7")
    assert list(prior["id"]) == ["e3", "e4", "e5", "e6"]
    assert (prior["possession"] == 2).all()


def test_prior_possession_of_first_possession_is_empty():
    assert get_prior_possession(EVENTS, "e1").empty


def test_prior_possession_unknown_event_id():
    prior = get_prior_possession(EVENTS, "not-a-real-id")
    assert isinstance(prior, pd.DataFrame)
    assert prior.empty
