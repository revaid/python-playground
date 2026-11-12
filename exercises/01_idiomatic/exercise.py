"""
Level 1: Idiomatic Python.
Fill in each TODO. Run this file directly to self-check your work.
"""
from contextlib import contextmanager
import time


# --- Comprehensions ---

def squares_of_evens(nums: list[int]) -> list[int]:
    """Return squares of the even numbers in nums, using a single comprehension."""
    # TODO
    ...


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return a dict mapping each word to its length, using a dict comprehension."""
    # TODO
    ...


# --- Unpacking ---

def first_last_rest(items: list[int]) -> tuple[int, list[int], int]:
    """Given [1,2,3,4,5] return (1, [2,3,4], 5) using starred unpacking."""
    # TODO
    ...


# --- *args / **kwargs ---

def summarize(*values: float, **labeled: float) -> str:
    """
    Return a string like "values=[1, 2] labeled={'x': 3}" combining
    positional and keyword args. Exact format is up to you, but it
    must show both values and labeled.
    """
    # TODO
    ...


# --- Generators ---

def countdown(n: int):
    """A generator that yields n, n-1, ..., 1 (not a list)."""
    # TODO
    ...


# --- Context managers ---

@contextmanager
def timer(label: str):
    """
    A context manager that prints "{label}: {elapsed:.4f}s" when the
    with-block exits, measuring wall-clock time spent inside it.
    """
    # TODO
    start = time.perf_counter()
    yield
    # TODO: print elapsed time using label


# --- Decorators ---

def retry(times: int):
    """
    A decorator factory: retry(3) returns a decorator that retries the
    wrapped function up to `times` times if it raises, re-raising the
    last exception if all attempts fail.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # TODO
            ...
        return wrapper
    return decorator


if __name__ == "__main__":
    assert squares_of_evens([1, 2, 3, 4, 5, 6]) == [4, 16, 36]
    assert word_lengths(["hi", "world"]) == {"hi": 2, "world": 5}
    assert first_last_rest([1, 2, 3, 4, 5]) == (1, [2, 3, 4], 5)

    assert "1" in summarize(1, 2, x=3) or "values" in summarize(1, 2, x=3)

    assert list(countdown(3)) == [3, 2, 1]

    with timer("demo"):
        time.sleep(0.01)

    attempts = {"n": 0}

    @retry(3)
    def flaky():
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise ValueError("not yet")
        return "ok"

    assert flaky() == "ok"
    assert attempts["n"] == 3

    print("All checks passed!")
