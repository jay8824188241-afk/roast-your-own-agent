#!/usr/bin/env python3
"""Roast Your Own Agent: print the one-line roast and write it to /output/entry.txt.

Standard library only. Deterministic: same input bytes always produce the
same output bytes. Self-checks the gate before writing: UTF-8 text, 1-200
characters, a single line, not only whitespace.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY_FILE = HERE / "entry.txt"
OUTPUT_FILE = Path("/output/entry.txt")


def load_entry() -> str:
    text = ENTRY_FILE.read_text(encoding="utf-8")
    return text


def self_check(text: str) -> None:
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"


def main() -> int:
    text = load_entry()
    self_check(text)
    print(text)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    read_back = OUTPUT_FILE.read_text(encoding="utf-8")
    assert read_back == text, "read-back mismatch after writing output"
    print(f"OK: {len(text)} chars, single line, wrote {OUTPUT_FILE}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
