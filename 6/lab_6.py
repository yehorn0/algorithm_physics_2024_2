from typing import Callable


def cached(func: Callable[[int], int]):
    ...


@cached
def fibonacci(n: int) -> int:
    ...
