# MethaneHunter — Project Status

## Current phase
Phase 0 — Milestone 0.1 DONE. Next: Milestone 0.2.

## Completed
- 0.1 Project skeleton, src/ layout, editable install, smoke test, ruff

## Verified results (0.1)
- check_environment.py: PASSED (Python 3.13.3, .venv on D:)
- pytest: 1 passed
- ruff check: all checks passed

## Environment
- Windows, PowerShell, VS Code + GitHub Desktop
- Python 3.13.3, venv at D:\Github\MethaneHunter\.venv
- C: drive is full; everything project-related lives on D:
  - TEMP/TMP = D:\tmp, PIP_CACHE_DIR = D:\pip-cache, HF_HOME = D:\hf-cache
- No GPU planned locally; Kaggle GPU for Phase 3 training

## Files
- pyproject.toml: package metadata, dependencies, pytest + ruff config
- src/methanehunter/__init__.py: package version
- scripts/check_environment.py: environment check (exit code 0/1)
- tests/test_smoke.py: import smoke test
- .gitignore: excludes .venv, caches, data/, mlruns/

## Decisions
- src/ layout, editable install; pyproject.toml is the single dependency source
- Code license MIT; dataset (MARS-S2L) CC BY-NC-SA 4.0, never committed
- Work only on a stratified 5–10k subset, never the full ~96 GB
- All caches and data on D: (C: has no free space)
- Run terminal commands one at a time

## Known issues
- C: drive at 0 GB free; some tools may still write there

## Next task
- Milestone 0.2: download only the metadata CSV and audit it (no images)

## Verified results (0.2)
- pytest: 5 passed
- Metadata CSV: data/raw/metadata/validated_images_all.csv (94.1 MB)
- Dataset revision: c26b1d7e31a0c5241fa37c9140802622c215eb32
- 93,538 rows, 6,053 plumes (6.5%), 0 duplicate ids
- Splits: train_2023 38,345 (9.2% plume, 2018–2023-11), val_2023 6,018 (5.0%, 2021),
  test_2023 43,524 (4.2%, 2024), Not Used 5,651 (excluded)
- Satellite shift: Landsat ~17% train, ~4% val, ~42% test; S2C only in test
- Unseen test sites: 697; 15,655 / 43,524 test rows
- Leakage proven: ch4path presence == isplume; observability non-clear ⇒ almost no plumes

## Decisions (0.2)
- Exclude split "Not Used"
- Leakage list extended: plumepath, window_row_off, window_col_off, window_width, window_height
- Thresholds/calibration tuned on val only; test keeps natural plume rate
- Report: all vs clear images; seen vs unseen sites; S2 vs Landsat

## Open issues
- ~16 rows with window_* but no ch4path
- background_image_tile missing for 3.3% — usable? correlated with label?
- Overlap between sector "Controlled Releases" and split "Not Used"