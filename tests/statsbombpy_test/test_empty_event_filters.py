from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch

import pandas as pd

from statsbombpy import sb


class TestEmptyEventFilters(TestCase):
    def setUp(self):
        self.events_by_match = {
            1: {
                "pass-event": {
                    "id": "pass-event",
                    "type": {"id": 30, "name": "Pass"},
                    "period": 1,
                    "match_id": 1,
                }
            },
            2: {
                "shot-event": {
                    "id": "shot-event",
                    "type": {"id": 16, "name": "Shot"},
                    "period": 1,
                    "match_id": 2,
                }
            },
        }
        events_patch = patch(
            "statsbombpy.public.events",
            side_effect=lambda match_id: deepcopy(self.events_by_match[match_id]),
        )
        events_patch.start()
        self.addCleanup(events_patch.stop)
        auth_patch = patch("statsbombpy.api_client.has_auth", return_value=False)
        auth_patch.start()
        self.addCleanup(auth_patch.stop)

    def competition_events(self, **kwargs):
        competition = {
            ("Test", "League", "2026", "male"): {"competition_id": 1, "season_id": 1}
        }
        with patch.object(sb, "competitions", return_value=competition), patch.object(
            sb, "matches", return_value={1: {}, 2: {}}
        ), patch.object(sb, "Pool") as pool:
            pool.return_value.__enter__.return_value.map.side_effect = (
                lambda call, match_ids: list(map(call, match_ids))
            )
            return sb.competition_events("Test", "League", "2026", creds={}, **kwargs)

    def test_events_returns_empty_dataframe_when_nothing_matches(self):
        for filters in ({"type": "Own Goal Against"}, {"period": 3}):
            with self.subTest(filters=filters):
                result = sb.events(1, filters=filters, creds={})
                self.assertIsInstance(result, pd.DataFrame)
                self.assertTrue(result.empty)

    def test_events_keeps_matching_events(self):
        result = sb.events(1, filters={"type": "Pass"}, creds={})
        self.assertEqual(result["id"].tolist(), ["pass-event"])
        self.assertEqual(result["match_id"].tolist(), [1])

    def test_events_split_returns_empty_dict(self):
        result = sb.events(1, filters={"type": "Own Goal Against"}, split=True, creds={})
        self.assertEqual(result, {})

    def test_competition_events_returns_empty_dataframe_when_nothing_matches(self):
        for filters in ({"type": "Own Goal Against"}, {"period": 3}):
            with self.subTest(filters=filters):
                result = self.competition_events(filters=filters)
                self.assertIsInstance(result, pd.DataFrame)
                self.assertTrue(result.empty)

    def test_competition_events_keeps_matches_with_results(self):
        result = self.competition_events(filters={"type": "Shot"})
        self.assertEqual(result["id"].tolist(), ["shot-event"])
        self.assertEqual(result["match_id"].tolist(), [2])

    def test_competition_events_split_returns_empty_dict(self):
        result = self.competition_events(filters={"type": "Own Goal Against"}, split=True)
        self.assertEqual(result, {})
