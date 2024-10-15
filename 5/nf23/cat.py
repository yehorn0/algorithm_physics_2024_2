from animal import Animal


class Cat(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name)
        self.__age = age

    def speak(self) -> None:
        print(f"Cat {self.name} says {self.__age} years old")

    def __str__(self) -> str:
        return f"Cat:{self.name}:{self.__age}"

def main() -> None:
    cat = Cat("Funny", 20)
    bird = Animal("Bird")

    cat.speak()
    bird.speak()

    print(isinstance(cat, Cat)) # True
    print(isinstance(cat, Animal)) # True
    print(isinstance(bird, Cat)) # False
    print(isinstance(bird, Animal)) # True
    print(issubclass(Cat, Animal))

if __name__ == '__main__':
    main()
