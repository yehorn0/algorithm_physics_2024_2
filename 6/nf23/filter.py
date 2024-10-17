from typing import Callable, TypeVar


T = TypeVar("T")

# std::vector<T>
def filter_function(func: Callable[[T], bool], arr: list[T] = None) -> list[T]:
    if not arr:
        arr = []

    return [
        elem for elem in arr if func(elem)
    ]


def is_odd(number: int) -> bool:
    return number % 2 != 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_function(is_odd, numbers))

filtered_numbers = filter(is_odd, numbers)
print(list(filtered_numbers))

filtered_numbers_with_lambda = filter(lambda x: x % 2 != 0, numbers)
print(list(filtered_numbers_with_lambda))
