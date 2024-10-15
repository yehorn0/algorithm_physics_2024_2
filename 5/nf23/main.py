from farm import Farm
from animal import Animal
from dog import Dog
from cat import Cat
from golden_retriever import GoldenRetriever


def main() -> None:

    # gr = GoldenRetriever("Dex", 20)
    gr = GoldenRetriever.__new__(GoldenRetriever)
    GoldenRetriever.__init__(gr, "Dex", 20)

    cat = Cat("Funny", 20)
    bird = Animal("Bird")
    dog = Dog("Lizzy", 15, "Jack Russel")

    farm = Farm()
    farm.add_animal(cat).add_animal(gr).add_animal(bird).add_animal(dog).add_food()

    farm.all_speak()

    print(farm)
    print([cat])


if __name__ == '__main__':
    main()
