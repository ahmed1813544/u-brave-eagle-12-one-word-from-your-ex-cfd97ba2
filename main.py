#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word an ex
would use to describe the entrant. Standard library only.

Why this word: it is the word an ex says when the relationship
was real to one person and provisional to the other — kept around
until someone better came along. It stings because it is true,
it lands instantly with no explanation, and everyone has either
been one or dated one. A sharp, self-deprecating self-portrait
in a single word, not an insult for its own sake.
"""

import os

WORD = "placeholder"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
