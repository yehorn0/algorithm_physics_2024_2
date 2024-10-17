from typing import Any, Callable, TypeVar



def reverse_not_clean(arr: list[Any]) -> None:
    for idx in range(len(arr) // 2):
        arr[idx], arr[len(arr) - idx - 1] = arr[len(arr) - idx - 1], arr[idx]


def reverse_clean(arr: list[Any]) -> list[Any]:
    return arr[::-1]


T = TypeVar("T")

# std::vector<T>
def square_array(func: Callable[[T], T], arr: list[T] = None) -> list[T]:
    if not arr:
        arr = []

    return [
        func(elem) for elem in arr
    ]




def main():
    # test_array = [1, 2, 3, 4, 5]
    #
    # # reverse_not_clean(test_array)
    # new_array = reverse_clean(test_array)
    #
    # print(test_array)
    # print(new_array)
    squared = square_array()
    print(squared)
    squared = square_array()
    print(squared)
    some_tuple = (1, 2, 3)
    #some_tuple[0] = 2
    some_tuple_with_list = (1, 2, [3, 4])
    some_tuple_with_list[2].append(5)
    print(some_tuple_with_list)

if __name__ == '__main__':
    main()
