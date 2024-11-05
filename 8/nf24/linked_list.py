from typing import Self
from node import Node


class LinkedList:
    def __init__(self):
        self.__len = 0
        self.__head: Node | None = None

    def __str__(self) -> str:
        # nodes = []
        # current = self.__head
        # while current:
        #     nodes.append(str(current))
        #     current = current.next

        return "->".join(str(node) for node in self)

    def append(self, data: int) -> None:
        if not self.__head:
            self.__head = Node(data)
        else:
            current = self.__head

            while current.next is not None:
                current = current.next

            current.next = Node(data)
        self.__len += 1

    def remove(self, data: int) -> None:
        error_str = f"LinkedList.remove({data}): {data} not in list"
        if not self.__head:
            raise ValueError(error_str)

        if self.__head.data == data:
            self.__len -= 1
            self.__head = self.__head.next
            return

        current = self.__head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            raise ValueError(error_str)
        else:
            self.__len -= 1
            current.next = current.next.next

    # ====================================================================================
    # ==================================== LAB 8 =========================================
    # ====================================================================================
    def reverse(self) -> Self:
        ...

    # ====================================================================================
    # ====================================================================================
    # ====================================================================================

    def __len__(self):
        # len_ = 0
        # current = self.__head
        #
        # while current:
        #     len_ += 1
        #     current = current.next
        #
        # return len_
        return self.__len

    def __getitem__(self, index: int) -> int:
        current_position = 0
        current = self.__head

        while current:
            if current_position == index:
                return current.data
            current = current.next
            current_position += 1

        raise IndexError(f"Linked list doesnt have index {index}")

    def __iter__(self):
        current = self.__head
        while current:
            yield current
            current = current.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.append(1)
    ll.append(3)
    ll.append(-100)
    ll.append(5)

    print(ll)
    print(f"Length: {len(ll)}")

    ll.remove(-100)
    print(ll)
    print(f"Length: {len(ll)}")

    ll.remove(1)
    print(ll)
    print(f"Length: {len(ll)}")
