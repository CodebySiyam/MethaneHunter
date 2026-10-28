"""Tests for metadata loading and validation."""

import pandas as pd
import pytest

from methanehunter.data.metadata import find_unseen_sites, load_metadata, validate_columns


def test_validate_columns_reports_missing() -> None:
    df = pd.DataFrame({"a": [1]})
    with pytest.raises(ValueError, match="b"):
        validate_columns(df, ["a", "b"])


def test_load_metadata_parses_dates_as_utc(tmp_path) -> None:
    csv_path = tmp_path / "meta.csv"
    pd.DataFrame(
        {"id_loc_image": ["x"], "tile_date": ["2024-06-13 10:00:31+00:00"]}
    ).to_csv(csv_path, index=False)

    df = load_metadata(csv_path, ["id_loc_image", "tile_date"])

    assert str(df["tile_date"].dt.tz) == "UTC"


def test_load_metadata_missing_file_raises(tmp_path) -> None:
    with pytest.raises(FileNotFoundError):
        load_metadata(tmp_path / "nope.csv", [])


def test_find_unseen_sites() -> None:
    df = pd.DataFrame(
        {
            "id_location": ["A", "B", "B", "C"],
            "split_name": ["train_2023", "train_2023", "test_2023", "test_2023"],
        }
    )
    assert find_unseen_sites(df, "train_2023", "test_2023") == {"C"}