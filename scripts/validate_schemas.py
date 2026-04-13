from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from zhumeng_qiangji_skill.schemas import validate_schema_file


def iter_schema_files(root: Path) -> list[Path]:
    files = sorted((root / "schemas").glob("*.json"))
    files.extend(sorted((root / "skills").glob("*/input_schema.json")))
    files.extend(sorted((root / "skills").glob("*/output_schema.json")))
    return files


def main() -> int:
    schema_files = iter_schema_files(ROOT)
    for path in schema_files:
        validate_schema_file(path)
        print(f"[ok] {path.relative_to(ROOT)}")
    print(f"validated {len(schema_files)} schema files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

