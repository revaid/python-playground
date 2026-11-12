# Python Expert Path

Roadmap to go from "knows the basics" to genuinely fluent Python.

## Levels

1. **Idiomatic Python** (`exercises/01_idiomatic`) — comprehensions, unpacking,
   `*args`/`**kwargs`, context managers, generators/iterators, decorators
2. **OOP done right** (`exercises/02_oop`) — dataclasses, dunder methods,
   composition vs inheritance, properties
3. **Ecosystem essentials** (`exercises/03_ecosystem`) — venvs, `pyproject.toml`
   packaging, type hints + `mypy`, `pytest`
4. **Real-world skills** (`exercises/04_real_world`) — error handling patterns,
   logging, files/APIs (`requests`, `json`), `asyncio` basics
5. **Specialty** — pick one after level 4: web (FastAPI/Django), data
   (pandas/numpy), automation/CLI (`typer`/`click`)

## Projects

- `projects/01_cli_tool` — a small CLI tool that forces you to combine
  argument parsing, file I/O, error handling, and tests.

## How to work through this

Each exercise folder has a `README.md` with the task and a starter `.py`
file with `# TODO` markers. Write your solution, then run the file —
most include a `if __name__ == "__main__":` self-check so you get instant
feedback without needing a test runner yet.

Work level by level. Don't skip to projects before finishing level 1-2 —
the idioms show up everywhere afterward.
