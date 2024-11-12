import email


class User:
    def __init__(self, username: str, name: str, email: str) -> None:
        self.__username: str = username
        self.__name:     str = name
        self.__email:    str = email

    def __repr__(self) -> str:
        return "User(username='{}', name='{}', email='{}')".format(
            self.__username, self.__name, self.__email
        )

    @property
    def username(self) -> str:
        return self.__username

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        # Consider adding validation using regexp
        self.__email = value

    def __str__(self) -> str:
        return self.__repr__()
