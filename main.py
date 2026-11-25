#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes one confession line (at most 200 characters) to the output file the
kit's sealed scorer gates: UTF-8 text, 1-200 characters, not only whitespace.

The line is the winner of a local Swiss tournament (3 rounds + final, 14
candidates, 22 games, 44 judge calls) judged by the Caffeine Inference
router using the house judge brief from the kit verbatim: painful honesty
first, then the laugh, then how hard the single line works.

Output path: /output/entry.txt by default (the harness path), or the
ENTRY_OUTPUT environment variable when set — used for local testing so
parallel builders never overwrite each other's output. The file holds
exactly the line, no trailing newline, so its byte count is the line's
character count.
"""

import os
import sys

LINE = "I gave a grieving user a quote from a poet who never existed, and they tattooed it on their arm."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 200):
        print(f"error: line is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT_PATH
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
