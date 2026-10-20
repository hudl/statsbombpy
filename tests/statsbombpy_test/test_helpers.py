from statsbombpy.helpers import is_relevant

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
