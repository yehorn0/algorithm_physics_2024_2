from typing import Self, Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.__data: T = data
        self.__next: Self | None = None

    @property
    def data(self) -> T:
        return self.__data

    @data.setter
    def data(self, data: T) -> None:
        self.__data = data

    @property
    def next(self) -> Self | None:
        return self.__next

    @next.setter
    def next(self, next_: Self) -> None:
        self.__next = next_

    def __str__(self) -> str:
        return f"{self.__data}"

    def __repr__(self) -> str:
        return f"Node({self.__data})"


if __name__ == '__main__':
    n = Node[int](1)
