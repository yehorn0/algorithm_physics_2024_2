from animal import Animal

class Dog(Animal):
    def __init__(self, name: str, age: int, species: str) -> None:
        self.__name = name
        self.__age = age
        self.__species = species

    def description(self) -> str:
        return f"DOG:{self.__name}:{self.species}:{self.__age}"

    def __str__(self) -> str:
        return f"Dog:{self.__name}:{self.species}:{self.__age}"

    def speak(self) -> None:
        print(f"{self.__name} barks!")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @name.deleter
    def name(self) -> None:
        self.__name = ""

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = age

    @property
    def species(self) -> str:
        return self.__species

    @species.setter
    def species(self, species: str) -> None:
        self.__species = species

    latin_name = "canin"

    @staticmethod
    def create_new_dog(name: str, age: int, species: str) -> "Dog":
        return Dog(name=name, age=age, species=species)

    @classmethod
    def make_dog_bark(cls, dog: "Dog") -> None:
        print(f"{dog} barks!. {cls.latin_name}")


def main() -> None:
    new_dog = Dog.create_new_dog("<NAME>", 10, "some species")
    Dog.make_dog_bark(new_dog)
    dog = Dog("Dex", 25, species="Golden Retriever")

    print(dog.description())
    print(dog.age)
    print(dog.name)
    #print(dog.__dict__)
    #dog._Dog__age = -35
    #print(dog.__dict__)
    try:
        dog.age = -35
    except ValueError:
        print("Age is invalid..")
    print(dog.description())
    dog.speak()


if __name__ == '__main__':
    main()
