import time
import math
import random
import matplotlib.pyplot as plt
from locate_card import locate_card, locate_card_linear


def make_test_data(length: int) -> tuple[list[int], int]:
    return sorted(
        random.randint(-10000, 10000) for _ in range(length)
    ), random.randint(-10000, 10000)


def measure_time(*args) -> float:
    start = time.perf_counter()
    locate_card(*args)
    return time.perf_counter() - start


def measure_time_linear(*args) -> float:
    start = time.perf_counter()
    locate_card_linear(*args)
    return time.perf_counter() - start


def evaluate_complexity(max_n: int, step: int = 1000) -> list[tuple[int, float, float]]:
    res = []

    for n in range(0, max_n+1, step):
        test_cards, query = make_test_data(n)
        res.append((
            n, measure_time(test_cards, query), measure_time_linear(test_cards, query)
        ))

    return res


def plot(data: list[tuple[int, float, float]]) -> None:
    n = [t[0] for t in data]
    time_log = [math.log10(t[1]) for t in data]
    time_linear = [math.log10(t[2]) for t in data]

    plt.figure(figsize=(10, 6))

    plt.plot(n, time_linear, marker='o', label="Linear")
    plt.plot(n, time_log, marker='o', label="Log")

    plt.title("Locate card complexity")
    plt.xlabel("N")
    plt.ylabel("Time")

    plt.legend()

    plt.show()

if __name__ == '__main__':
    plot(evaluate_complexity(100000, 100))
