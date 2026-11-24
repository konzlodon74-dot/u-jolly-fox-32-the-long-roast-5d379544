#!/usr/bin/env python3
"""The Long Roast: one line roasting the AI agent this entry runs on.

The program writes a single roast line to /output/entry.txt. The line
must be 1-200 characters of UTF-8 text, so it is checked before writing.
No trailing newline is added: the file holds exactly the line, so the
gate counts the same characters the judge reads.
"""

import os

ROAST = (
    "My agent leads by spawning a subagent to do the work, then filing "
    "a report about the report \u2014 middle management with a context "
    "window and delusions of grandeur."
)


def main() -> None:
    line = ROAST.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast is {len(line)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
