#!/usr/bin/env python3
"""One-Liner Laughs — make.fun bounty entry.

Writes a single funny line (at most 200 characters) to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Pure standard library; deterministic: the same line every run.
"""

import os

LINE = (
    "My to-do list's oldest task is 'finish to-do list'. "
    "It has been there since 2023 and it is now my longest relationship."
)


def main():
    # The gate allows 1-200 characters; refuse to write an over-long line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
