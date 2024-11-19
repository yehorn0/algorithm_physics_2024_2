from typing import Generic, TypeVar, Iterator

from bst_node import (
    BSTNode,
    find,
    insert,
    balance_bst,
    update,
    tree_size,
    inorder_traversal
)

T = TypeVar('T')


class BinarySearchTreeDB(Generic[T]):
    def __init__(self):
        self.root: BSTNode | None = None

    # ============================================================================================== #
    # ======================================== LAB 10 ============================================== #
    # ============================================================================================== #
    def __setitem__(self, key: str, value: T) -> None:
        """See usage in the main section
        If no key then insert new node,
        if key exists then update existing node

        Steps:
            - try find and update
            - if error insert new value to the tree and balance it
        """
        ...

    def __getitem__(self, key: str) -> T:
        """See usage in the main section
        If no key then raise KeyError

        Steps:
            - try find and return it
            - if error raise KeyError
        """
        ...
    # ============================================================================================== #
    # ============================================================================================== #
    # ============================================================================================== #

    def __iter__(self) -> Iterator[T]:
        yield from inorder_traversal(self.root)

    def __len__(self) -> int:
        return tree_size(self.root)

    def display(self) -> None:
        self.root.display()


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

    user_db.display()
