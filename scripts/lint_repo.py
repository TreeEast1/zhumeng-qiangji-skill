from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "rules" / "routing_rules.yaml",
    ROOT / "prompts" / "system_prompt.md",
    ROOT / "schemas" / "answer.schema.json",
    ROOT / "knowledge" / "mock" / "schools.demo.yaml",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    if missing:
        for path in missing:
            print(f"[missing] {path.relative_to(ROOT)}")
        return 1

    for path in (ROOT / "knowledge" / "mock").glob("*.yaml"):
        content = path.read_text(encoding="utf-8")
        if "Demo/mock data only" not in content:
            print(f"[missing disclaimer] {path.relative_to(ROOT)}")
            return 1

    print("[ok] repository lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

