from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from zhumeng_qiangji_skill.guardrails import inspect_answer


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local guardrail checks.")
    parser.add_argument("--query", default="", help="Original user query.")
    parser.add_argument("--answer", required=True, help="Candidate answer to inspect.")
    args = parser.parse_args()

    result = inspect_answer(args.query, args.answer)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

