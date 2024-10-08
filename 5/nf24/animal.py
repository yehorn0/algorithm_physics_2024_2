class Animal:
    def speak(self) -> None:
        print("Animal speaks")

    def description(self) -> str:
        return "ANIMAL"

    def __str__(self) -> str:
        return "Animal"

    def __repr__(self) -> str:
        return "ANIMAL"
