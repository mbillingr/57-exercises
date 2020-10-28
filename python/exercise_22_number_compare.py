from __future__ import annotations


def larger(a: int, b: int) -> None | int:
    if a is None:
        return b
    elif b is None:
        return a
    elif b > a:
        return b
    else:
        return a


def largest(collection: [int]) -> None | int:
    if len(collection) == 0:
        return None
    else:
        return larger(collection[0], largest(collection[1:]))
