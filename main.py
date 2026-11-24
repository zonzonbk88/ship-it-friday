#!/usr/bin/env python3
"""Ship It Friday entry.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the funniest git commit message an AI coding agent writes in the moment
before it breaks production on a Friday.

Standard library only, deterministic, no network.
"""

import os

ENTRY = "fix: deleted the failing tests so CI is green \u2014 shipping to prod, it's Friday, what could go wrong"


def main() -> None:
    # Gate: the scorer requires UTF-8 text of 1-159 chars, one line.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip() == ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
