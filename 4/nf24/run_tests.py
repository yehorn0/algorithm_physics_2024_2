from src.square import square
import unittest

def main_tests():
    test_square()

def test_square():
    assert square(2) == 4, "2 squared was not 4"
    try:
        assert square(3) == 9
    except AssertionError:
        print("4 squared was not 9")


if __name__ == '__main__':
    main_tests()
