"""Smoke test: confirms the package is installed and importable."""

import methanehunter


def test_package_has_version() -> None:
    assert methanehunter.__version__ == "0.1.0"
    