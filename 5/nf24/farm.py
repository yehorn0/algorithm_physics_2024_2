from animal import Animal
from dog import Dog
from cat import Cat
from golden_retriever import GoldenRetriever


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal) -> "Farm":
        self.animals.append(animal)
        return self

    def all_speak(self):
        for animal in self.animals:
            animal.speak()

    def descriptions(self) -> str:
        return ", ".join(f"{animal}" for animal in self.animals)




def main() -> None:
    dog_dex = GoldenRetriever("Dex", 25)
    dog_lizzie = Dog("Lizzie", 15, species="Jack Russel")

    cat_fanny = Cat("Fanny")

    unknown_animal = Animal()

    farm = (Farm().add_animal(dog_dex).add_animal(dog_lizzie).
            add_animal(cat_fanny).add_animal(unknown_animal))

    farm.all_speak()

    print(f"Farm: {farm.descriptions()}")



if __name__ == '__main__':
    main()
