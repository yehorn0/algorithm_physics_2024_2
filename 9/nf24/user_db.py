from user import User


class UserDatabase:
    def __init__(self) -> None:
        self.__users: list[User] = []

    def insert(self, user: User) -> None:
        """Time: O(n), space: O(1)
        """
        current_pos: int = 0
        while current_pos < len(self.__users):
            # Find the first username greater than the new user's username
            if self.__users[current_pos].username > user.username:
                break
            current_pos += 1
        self.__users.insert(current_pos, user)

    def find(self, username: str) -> User:
        """Time: O(n), space: O(1)
        """
        for user in self.__users:
            if user.username == username:
                return user

        raise ValueError(f'User {username} not found')

    def update(self, user: User) -> None:
        """Time: O(n), space: O(1)
        """
        target = self.find(user.username)

        target.name, target.email = user.username, user.email


    def list_all(self) -> list[User]:
        """Time: O(1), space: O(1)
        """
        return self.__users


if __name__ == '__main__':
    user_0 = User("user0", "User 0","user0@example.com")
    user_1 = User("user1", "User 1","user1@example.com")
    user_2 = User("user2", "User 2","user2@example.com")
    user_3 = User("user3", "User 3","user3@example.com")

    user_db = UserDatabase()

    user_db.insert(user_0)
    user_db.insert(user_1)
    user_db.insert(user_2)
    user_db.insert(user_3)

    user_found = user_db.find("user1")
    print(user_found)
    print(user_db.list_all())