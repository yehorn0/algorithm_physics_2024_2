from typing import Callable, TypeVar


T = TypeVar("T")

# std::vector<T>
def map_function(func: Callable[[T], T], arr: list[T] = None) -> list[T]:
    if not arr:
        arr = []

    return [
        func(elem) for elem in arr
    ]


def square(x: T) -> T:
    return x * x


def cubed(x: T) -> T:
    return x ** 3


def linear_function(x: T) -> T:
    return 5*x + 4


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_number = map_function(square, numbers)

print(squared_number)

squared_numbers_map = map(square, numbers)

for elem in squared_numbers_map:
    print(elem, end=" ")

print()
# print(squared_numbers_map)
print(list(squared_numbers_map)) # [] ?? Why empty?


squared_number_with_lambda = map(lambda x: x * x, numbers)
cubed_number_with_lambda = map(lambda x: x ** 3, numbers)
linear_number_with_lambda = map(lambda x: 5*x + 4, numbers)
