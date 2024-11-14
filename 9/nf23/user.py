class User:
    def __init__(self, username: str, name: str, email: str) -> None:
        self.__username: str = username
        self.__name: str = name
        self.__email: str = email

    @property
    def key(self) -> str:
        return self.__username

    def update(self, other: "User") -> None:
        if self.key != other.key:
            raise ValueError("Keys don't match")
        self.__name = other.name
        self.__email = other.email

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    def __repr__(self) -> str:
        return f"<User(username={self.__username}, name={self.__name}, email={self.__email})>"
