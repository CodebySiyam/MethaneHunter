"""Download the MARS-S2L metadata CSV only (no images)."""

import sys
from pathlib import Path

from huggingface_hub import HfApi

from methanehunter.config import load_config
from methanehunter.data.metadata import download_metadata

CONFIG_PATH = Path("configs/data.yaml")


def main() -> int:
    cfg = load_config(CONFIG_PATH)
    ds = cfg["dataset"]
    try:
        info = HfApi().dataset_info(ds["repo_id"], revision=ds["revision"])
        path = download_metadata(
            repo_id=ds["repo_id"],
            filename=ds["metadata_filename"],
            local_dir=cfg["paths"]["metadata_dir"],
            repo_type=ds["repo_type"],
            revision=ds["revision"],
        )
    except Exception as exc:  # network or Hub errors: report clearly, exit non-zero
        print(f"Download failed: {type(exc).__name__}: {exc}")
        return 1

    print(f"Saved to: {path}")
    print(f"Size: {path.stat().st_size / 1e6:.1f} MB")
    print(f"Dataset commit (record this in PROJECT_STATUS.md): {info.sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())