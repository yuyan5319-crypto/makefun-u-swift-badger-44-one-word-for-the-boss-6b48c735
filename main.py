#!/usr/bin/env python3
"""One Word for the Boss.

Writes exactly one word describing the boss to the output file.

The word: Rescheduler.

Why this word: every office has one -- the boss whose signature move is
never keeping the original time. The meeting was Tuesday, then Thursday,
then "let's circle back next week". It is a single word a person would
actually use about the one they report to, it lands on its own at lunch,
it catches a real, specific boss habit, and it is not the first word
anyone reaches for.

Stdlib only: the grader runs a bare Python image with no third-party
packages installed.
"""

import os
import sys

WORD = "Rescheduler"

MAX_CHARS = 30


def validate(word):
    """Enforce the competition gate: one word, 1-30 chars, no whitespace."""
    if not word:
        raise ValueError("word must not be empty")
    if len(word) > MAX_CHARS:
        raise ValueError("word is %d chars, over the 30-char cap" % len(word))
    if word != word.strip():
        raise ValueError("word must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no spaces")
    if not word.isalpha():
        raise ValueError("word must be letters only, no digits or punctuation")
    return word


def output_path():
    """The grader reads /output/entry.txt; honour MAKEFUN_OUTPUT_DIR if set."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    word = validate(WORD)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(word)
    # Read it back and re-validate: the file on disk is what gets judged,
    # so a write that silently truncated or mangled it must fail loudly.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if validate(written) != word:
        raise ValueError("round-trip check failed: file holds %r" % written)
    print(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
