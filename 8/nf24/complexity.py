import math
from typing import Callable
import matplotlib.pyplot as plt


def plot(functions: list[Callable[[float], float]]) -> None:
    xs = list(range(10, 10000, 100))
    plt.figure(figsize=(10, 6))

    for func in functions:
        plt.plot(xs, [func(x) for x in xs])

    plt.title("Big-small-O")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.legend()

    plt.show()

if __name__ == '__main__':
    functions = [
        # lambda x: math.exp(x),
        # lambda x: 2**x,
        lambda x: x**2,
        lambda x: x * math.log10(x),
        # lambda x: 0.1*x,
        # lambda x: math.sqrt(x),
        # lambda x: 10*math.log(x),
    ]

    plot(functions)

