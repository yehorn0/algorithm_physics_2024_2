def main() -> None:
    x = int(input("Enter number: "))

    print(f"x squared is {square(x)}")


def square(n: int) -> int:
    return n ** 2


if __name__ == '__main__':
    main()
