from animal import Animal
from cat import Cat


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name)
        self._age = age
        self.__breed = breed

    def speak(self) -> None:
        print(f"Dog [{self.__breed}] {self.name} says {self._age} years old")

    def __str__(self) -> str:
        return f"Dog [{self.__breed}] {self.name}"



def main() -> None:
    dog = Dog("Dex", 20, "Golden Retriever")
    bird = Animal("Bird")

    dog.speak()
    bird.speak()
    print(isinstance(dog, Cat))
    # print(isinstance(cat, Cat)) # True
    # print(isinstance(cat, Animal)) # True
    # print(isinstance(bird, Cat)) # False
    # print(isinstance(bird, Animal)) # True
    # print(issubclass(Cat, Animal))

if __name__ == '__main__':
    main()
