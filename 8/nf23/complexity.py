import math
import matplotlib.pyplot as plt
from typing import Callable


def draw_functions(functions: list[Callable[[float], float]]) -> None:
    xs = list(range(10, 10000, 100))

    plt.figure(figsize=(10, 6))

    for func in functions:
        plt.plot(xs, [math.log10(func(xs)) for xs in xs])

    plt.title("Big-small-o")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.legend()

    plt.show()


if __name__ == '__main__':
    functions = [
        lambda x: 2*x - 3,
        lambda x: math.log(x) + 4
        # lambda x: 3*x*x + x - 5,
        # lambda x: 50*x*math.log(x) - x + 2,
    ]

    draw_functions(functions)
