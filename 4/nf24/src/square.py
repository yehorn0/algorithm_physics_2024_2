def main() -> None:
    x = int(input("Enter a number: "))
    print(f"The square of {x} is {square(x)}")


def square(n: int) -> int:
    return n * n + 1


if __name__ == "__main__":
    main()
