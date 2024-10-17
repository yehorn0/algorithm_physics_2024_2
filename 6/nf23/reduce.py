from typing import Callable, TypeVar

from functools import reduce


T = TypeVar("T")

# std::vector<T>
def reduce_function(func: Callable[[T, T], T], arr: list[T], initial: T | None = None) -> T:
    if initial:
        result = initial
    else:
        result = next(iter(arr))

    for elem in arr:
        result = func(result, elem)

    return result


def double_sum(number1: int, number2: int) -> int:
    return number1 * number2


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reduce_function(double_sum, numbers, -1))
print(reduce(double_sum, numbers))
print(reduce(lambda x, y: x * y, numbers, -1))
