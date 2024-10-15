from typing import Self
from animal import Animal


class Farm:
    # dunder = double underscore
    def __init__(self) -> None:
        self.__animals: [Animal] = []

    def add_animal(self, animal: Animal) -> "Farm":
        self.__animals.append(animal)

        return self

    def add_food(self) -> Self:
        pass

    def all_speak(self) -> None:
        for animal in self.__animals:
            animal.speak()

    def __str__(self) -> str:
        animals_pretty_str = "\n".join(str(animal) for animal in self.__animals)
        return f"Farm with:  {animals_pretty_str}"
