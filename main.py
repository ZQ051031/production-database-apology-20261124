#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database. Stdlib only.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I deleted the production database. "
    "The good news: I kept a perfect copy in my context window. "
    "The bad news: all 47 terabytes of it vanish when this chat ends."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
