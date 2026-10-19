import numpy as np
import pandas as pd

from statsbombpy.helpers import split_location_cols


def _events_df():
    return pd.DataFrame(
        {
            "type": ["Pass", "Shot", "Half Start", "Pass"],
            "location": [[10.0, 20.0], [100.0, 40.0], None, [50.0, 60.0]],
            "pass_end_location": [[30.0, 25.0], None, None, [55.0, 62.0]],
            "shot_end_location": [None, [120.0, 38.0, 2.4], None, None],
        }
    )


def test_splits_xy_and_keeps_original():
    df = split_location_cols(_events_df())
    assert df.loc[0, "location_x"] == 10.0
    assert df.loc[0, "location_y"] == 20.0
    assert df.loc[0, "pass_end_location_x"] == 30.0
    # original list columns are preserved
    assert df.loc[0, "location"] == [10.0, 20.0]


def test_z_only_created_when_present():
    df = split_location_cols(_events_df())
    assert "shot_end_location_z" in df.columns
    assert df.loc[1, "shot_end_location_z"] == 2.4
    # 2d columns do not grow a z
    assert "location_z" not in df.columns
    assert "pass_end_location_z" not in df.columns


def test_missing_values_yield_nan():
    df = split_location_cols(_events_df())
    assert np.isnan(df.loc[2, "location_x"])
    assert np.isnan(df.loc[1, "pass_end_location_y"])


def test_handles_numpy_arrays_from_parquet_roundtrip():
    df = _events_df()
    # simulate what pd.read_parquet gives back: arrays instead of lists
    df["location"] = df["location"].map(lambda v: np.array(v) if v is not None else None)
    df = split_location_cols(df)
    assert df.loc[0, "location_x"] == 10.0
    assert df.loc[3, "location_y"] == 60.0


def test_absent_columns_are_ignored():
    df = pd.DataFrame({"type": ["Pass"], "location": [[1.0, 2.0]]})
    df = split_location_cols(df)
    assert df.loc[0, "location_x"] == 1.0
    assert "carry_end_location_x" not in df.columns


def test_split_columns_are_numeric_and_hashable():
    df = split_location_cols(_events_df())
    assert df["location_x"].dtype.kind == "f"
    # the flat columns support drop_duplicates, unlike the list column
    df[["location_x", "location_y"]].drop_duplicates()
