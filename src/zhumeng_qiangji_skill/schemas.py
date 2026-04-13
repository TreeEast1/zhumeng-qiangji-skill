from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from .paths import repo_root


def load_schema(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_schema_file(path: Path) -> None:
    schema = load_schema(path)
    Draft202012Validator.check_schema(schema)


def validate_payload(schema_name: str, payload: dict) -> None:
    schema = load_schema(repo_root() / "schemas" / schema_name)
    validator = Draft202012Validator(schema)
    validator.validate(payload)

