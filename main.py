#!/usr/bin/env python3
"""Rejected Olympic Sports entry: Competitive Context Window.

Writes one funny single-line rejected Olympic sport to entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
"""
import os

ENTRY = "Competitive Context Window: athletes cram 94,208 tokens into one prompt, then forget the question before the judge finishes reading it."
# 135 chars, one line: a rejected Olympic sport the agent itself would lose.
# The athletes are agents; the event is their own context window turning on them.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
