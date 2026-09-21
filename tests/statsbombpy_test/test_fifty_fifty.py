import json
import warnings
from unittest import TestCase
from unittest.mock import patch

from requests import Response

from statsbombpy import api_client, sb
from statsbombpy.config import OPEN_DATA_PATHS


class TestFiftyFiftyEvents(TestCase):
    def setUp(self):
        # Reduced provider-shaped records; all event and match IDs are synthetic.
        self.match_id = 990101
        self.outcomes = [
            {"id": 1, "name": "Lost"},
            {"id": 2, "name": "Success To Opposition"},
            {"id": 3, "name": "Success To Team"},
            {"id": 4, "name": "Won"},
        ]
        self.fifty_fifty = [
            {
                "id": f"00000000-0000-4000-8000-{index:012d}",
                "type": {"id": 33, "name": "50/50"},
                "50_50": {"outcome": outcome},
            }
            for index, outcome in enumerate(self.outcomes, start=1)
        ]
        self.controls = [
            {
                "id": "00000000-0000-4000-8000-000000000005",
                "type": {"id": 30, "name": "Pass"},
                "pass": {"length": 12.5},
            },
            {
                "id": "00000000-0000-4000-8000-000000000006",
                "type": {"id": 23, "name": "Goal Keeper"},
                "goalkeeper": {"type": {"id": 33, "name": "Shot Faced"}},
            },
            {
                "id": "00000000-0000-4000-8000-000000000007",
                "type": {"id": 42, "name": "Ball Receipt*"},
                "ball_receipt": {"outcome": {"id": 9, "name": "Incomplete"}},
            },
        ]
        self.response = Response()
        self.response.status_code = 200
        self.response._content = json.dumps(self.fifty_fifty + self.controls).encode()

        def get_response(url, *args, **kwargs):
            self.assertEqual(
                url, OPEN_DATA_PATHS["events"].format(match_id=self.match_id)
            )
            # Response.json() decodes fresh records for each call.
            return self.response

        get_patch = patch("statsbombpy.public.req.get", side_effect=get_response)
        get_patch.start()
        self.addCleanup(get_patch.stop)
        warning_context = warnings.catch_warnings()
        warning_context.__enter__()
        self.addCleanup(warning_context.__exit__, None, None, None)
        warnings.simplefilter("ignore", api_client.NoAuthWarning)

    def events(self, **kwargs):
        return sb.events(self.match_id, creds={}, **kwargs)

    def assert_flat_outcomes(self, frame):
        self.assertIn("50_50_outcome", frame.columns)
        self.assertNotIn("50_50", frame.columns)
        rows = frame.loc[frame["type"] == "50/50"]
        self.assertEqual(rows["id"].tolist(), [e["id"] for e in self.fifty_fifty])
        self.assertEqual(rows["match_id"].tolist(), [self.match_id] * 4)
        self.assertEqual(
            rows["50_50_outcome"].tolist(), [o["name"] for o in self.outcomes]
        )

    def test_default_flattens_fifty_fifty_outcomes(self):
        frame = self.events()
        self.assertEqual(len(frame), 7)
        self.assert_flat_outcomes(frame)

    def test_split_preserves_group_name_and_flattens_outcomes(self):
        groups = self.events(split=True)
        self.assertIn("50/50s", groups)
        self.assert_flat_outcomes(groups["50/50s"])

    def test_type_filter_flattens_fifty_fifty_outcomes(self):
        frame = self.events(filters={"type": "50/50"})
        self.assertEqual(len(frame), 4)
        self.assert_flat_outcomes(frame)

    def test_explicit_nested_mode_preserves_outcome_objects(self):
        frame = self.events(flatten_attrs=False)
        self.assertNotIn("50_50_outcome", frame.columns)
        rows = frame.loc[frame["type"] == "50/50", "50_50"]
        self.assertEqual(rows.tolist(), [{"outcome": o} for o in self.outcomes])

    def test_json_preserves_raw_event_attributes(self):
        raw = self.events(fmt="json")
        self.assertEqual(len(raw), 7)
        for event in self.fifty_fifty:
            self.assertEqual(raw[event["id"]], dict(event, match_id=self.match_id))

    def test_existing_attribute_aliases_still_flatten(self):
        frame = self.events().set_index("type")
        self.assertEqual(frame.loc["Pass", "pass_length"], 12.5)
        self.assertEqual(frame.loc["Goal Keeper", "goalkeeper_type"], "Shot Faced")
        self.assertEqual(frame.loc["Ball Receipt*", "ball_receipt_outcome"], "Incomplete")

    def test_match_without_fifty_fifty_has_no_outcome_column(self):
        self.response._content = json.dumps(self.controls).encode()
        frame = self.events()
        self.assertEqual(len(frame), 3)
        self.assertNotIn("50_50", frame.columns)
        self.assertNotIn("50_50_outcome", frame.columns)
