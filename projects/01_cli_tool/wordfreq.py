"""
Project 1: Word Frequency CLI.
Fill in each TODO to make this tool work end to end.
"""
import argparse
import sys
from collections import Counter
from pathlib import Path


def extract_words(text: str) -> list[str]:
    """Lowercase, strip punctuation, split into words."""
    # TODO
    ...


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most common (word, count) pairs."""
    # TODO
    ...


def main() -> int:
    parser = argparse.ArgumentParser(description="Show the most common words in a file.")
    parser.add_argument("file", type=Path, help="path to a text file")
    parser.add_argument("--top", type=int, default=10, help="how many words to show")
    args = parser.parse_args()

    # TODO: read args.file, handle missing/empty file cleanly (no traceback),
    # print top_words(...) one per line as "word: count", return 0 on success
    # and 1 on error.
    ...


if __name__ == "__main__":
    sys.exit(main())
