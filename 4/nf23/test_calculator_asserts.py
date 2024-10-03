from src.calculations import square


def main() -> None:
    test_square()


def test_square() -> None:
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(5) != 25:
    #     print("5 squared was not 25")
    # assert False, "Assert error for False"
    assert square(2) == 4

    try:
        assert square(5) == 25
    except AssertionError:
        print("5 squared was not 25")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

if __name__ == '__main__':
    main()