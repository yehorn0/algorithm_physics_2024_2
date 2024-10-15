from abc import ABC, abstractmethod
from typing import Protocol


class AnimalProtocol(Protocol):
    def speak(self) -> None:
        ...

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self) -> None:
        ...


class Animal(AnimalProtocol):
    def __init__(self, name):
        self.__name = name

    def speak(self) -> None:
        print(f"Animal {self.__name} speaks")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name.capitalize()

    def __str__(self) -> str:
        return f"Animal: {self.__name}"

    def __repr__(self) -> str:
        return f"ANI:{self.__name}"
