"""
Tests for wordfreq.py. Run with: pytest
Fill these in once extract_words / top_words are implemented.
"""
from wordfreq import extract_words, top_words


def test_extract_words_lowercases_and_strips_punctuation():
    # TODO: assert extract_words("Hello, world! Hello?") == ["hello", "world", "hello"]
    ...


def test_top_words_counts_correctly():
    text = "a b a c a b"
    # TODO: assert top_words(text, 2) == [("a", 3), ("b", 2)]
    ...
