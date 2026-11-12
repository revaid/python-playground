# Project 1 — Word Frequency CLI

Build a CLI tool: `wordfreq <file.txt> [--top N]` that reads a text file and
prints the N most common words (default 10) with their counts.

Forces you to combine:
- argument parsing (`argparse`)
- file I/O with proper error handling (missing file, empty file)
- comprehensions / `collections.Counter`
- a basic test with `pytest`

## Requirements

- `python wordfreq.py sample.txt` → prints top 10 words and counts
- `python wordfreq.py sample.txt --top 3` → prints top 3
- Words are lowercased, punctuation stripped
- Missing file → clean error message, exit code 1 (no stack trace)
- Include at least 2 tests in `test_wordfreq.py`

## Run

```
python wordfreq.py sample.txt --top 5
pytest
```
