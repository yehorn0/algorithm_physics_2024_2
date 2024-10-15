from animal import Animal
from dog import Dog


class GoldenRetriever(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, "Golden Retriever")

    def __str__(self):
        return f"GR:{self.name}:{self._age}"


def main() -> None:
    gr = GoldenRetriever("Dex", 20)

    gr.speak()
    print(isinstance(gr, GoldenRetriever))
    print(isinstance(gr, Dog))
    print(isinstance(gr, Animal))


if __name__ == '__main__':
    main()
