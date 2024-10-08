from animal import Animal


class Cat(Animal):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    def speak(self) -> None:
        print(f"{self.name} says meow")

    def description(self) -> str:
        return f"CAT:{self.name}"

    def __str__(self) -> str:
        return f"Cat:{self.name}"