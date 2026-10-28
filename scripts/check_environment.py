"""Phase 0 environment check: verifies Python version and core packages."""

import sys
from importlib.metadata import PackageNotFoundError, version

MIN_PYTHON = (3, 10)
REQUIRED_PACKAGES = ["numpy", "pandas", "huggingface_hub", "pytest", "ruff"]


def check_python() -> bool:
    """Return True if the running Python meets the minimum version."""
    print(f"Python {sys.version.split()[0]} ({sys.executable})")
    if sys.version_info[:2] < MIN_PYTHON:
        print(f"  FAIL  Python >= {MIN_PYTHON[0]}.{MIN_PYTHON[1]} required")
        return False
    return True


def check_packages(packages: list[str]) -> bool:
    """Return True if all packages are installed; print each version."""
    all_ok = True
    for name in packages:
        try:
            print(f"  OK    {name} {version(name)}")
        except PackageNotFoundError:
            print(f"  FAIL  {name} is not installed")
            all_ok = False
    return all_ok


def check_project_package() -> bool:
    """Return True if the methanehunter package is importable."""
    try:
        import methanehunter
    except ImportError as exc:
        print(f"  FAIL  methanehunter not importable: {exc}")
        return False
    print(f"  OK    methanehunter {methanehunter.__version__}")
    return True


def main() -> int:
    results = [check_python(), check_packages(REQUIRED_PACKAGES), check_project_package()]
    print("\nEnvironment check PASSED" if all(results) else "\nEnvironment check FAILED")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())