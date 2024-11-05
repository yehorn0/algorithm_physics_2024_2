from typing import Self


class Node:
    def __init__(self, data: int) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self) -> int:
        return self.__data

    @data.setter
    def data(self, data: int) -> None:
        self.__data = data

    @property
    def next(self) -> Self | None:
        return self.__next

    @next.setter
    def next(self, next_: Self) -> None:
        self.__next = next_

    def __str__(self) -> str:
        return f"Node({self.__data})"
