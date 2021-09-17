from typing import Iterable, TypeVar

T = TypeVar("T")

def first(n: int, iter: Iterable[T]) -> T:
    for ind, i in enumerate(iter):
        if ind == n - 1:
            return
        yield i
