from dog import Dog


class GoldenRetriever(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, "Golden Retriever")
