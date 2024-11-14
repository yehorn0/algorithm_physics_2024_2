from typing import TypeVar, Generic, Protocol
from user import User


class DatabaseElementProtocol(Protocol):
    @property
    def key(self) -> str:
        ...

    def update(self, other: "DatabaseElementProtocol") -> None:
        ...


T = TypeVar('T', bound=User)


class Database(Generic[T]):
    def __init__(self) -> None:
        self.__elements: list[T] = [] # len = n

    def insert(self, element: T) -> None:
        # Time: O(n), Space: O(1)
        current_pos: int = 0

        while current_pos < len(self.__elements):
            if self.__elements[current_pos].key > element.key:
                break
            current_pos += 1

        self.__elements.insert(current_pos, element)

    def find(self, key: str) -> T:
        # Time: O(n), Space: O(1)
        for element in self.__elements:
            if element.key == key:
                return element

        raise ValueError(f"Element with key {key} not found")

    def update(self, element: T) -> None:
        # Time: O(n), Space: O(1)
        target: T = self.find(element.key)

        target.update(element)

    def list_all(self) -> list[T]:
        # Time: O(1), Space: O(1)
        return self.__elements


if __name__ == '__main__':
    user0 = User("user0", "User 0", email="user0@example.com")
    user1 = User("user1", "User 1", email="user1@example.com")
    user2 = User("user2", "User 2", email="user2@example.com")
    user3 = User("user3", "User 3", email="user3@example.com")

    user_db = Database[User]()

    user_db.insert(user0)
    user_db.insert(user1)
    user_db.insert(user2)
    user_db.insert(user3)

    print(user_db.list_all())

    user3_updated = User("user3", "User 3 updated", email="user3_new@example.com")
    user_db.update(user3_updated)

    print(user_db.list_all())
