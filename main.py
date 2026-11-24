#!/usr/bin/env python3
"""The Perfect Pickup Line — entry program.

Writes one original pickup line, voiced as an AI agent speaking to a
person, to /output/entry.txt. The line is fixed: every run writes the
same bytes, so the two grading runs agree exactly.
"""

import os

LINE = (
    # Setup promises a machine-perfect answer; the turn is humble
    # instead: a million simulations, and the ending is only a hope.
    # Machine-voiced, one breath, flattering, no pressure to answer.
    "I ran a million simulations of this exact moment \u2014 in every "
    "single one, I still ended up hoping you'd say hi back."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1 to 200 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
