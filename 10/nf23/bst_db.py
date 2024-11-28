from typing import Generic, TypeVar, Iterator

from bst_node import (
    BSTNode,
    display,
    insert,
    update,
    find,
    list_all,
    tree_size
)
from balanced import make_balanced


T = TypeVar('T')


class BinarySearchTreeDB(Generic[T]):
    def __init__(self) -> None:
        self.__root: BSTNode[T] | None = None

    def __setitem__(self, key: str, value: T) -> None:
        try:
            node = find(self.__root, key)
            update(node, value)
        except KeyError:
            if not self.__root:
                self.__root = BSTNode(value)
            else:
                insert(self.__root, value)
                self.__root = make_balanced(list_all(self.__root))

    def __getitem__(self, key: str) -> T:
        return find(self.__root, key)

    def __len__(self) -> int:
        return tree_size(self.__root)

    def __iter__(self) -> Iterator[T]:
        yield from list_all(self.__root)

    def display(self) -> None:
        display(self.__root)


if __name__ == '__main__':
    from user import User
    user_db = BinarySearchTreeDB[User]()
    user0 = User("user0", "User 0", email="user0@example.com")
    user1 = User("user1", "User 1", email="user1@example.com")
    user2 = User("user2", "User 2", email="user2@example.com")
    user3 = User("user3", "User 3", email="user3@example.com")
    user_db[user0.key] = user0
    user_db[user1.key] = user1
    user_db[user2.key] = user2
    user_db[user3.key] = user3
    print(len(user_db))
    user_db.display()
