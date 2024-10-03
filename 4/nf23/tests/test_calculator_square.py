from typing import Callable

import unittest


class CalculatorSquareTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tested_function = self._build_test_function()

    def tearDown(self) -> None:
        # print("teardown")
        pass

    def _build_test_function(self) -> Callable[[int], int]:
        from src.calculations import square
        return square

    def test_positive_number(self):
        """Test for positive number
        """
        # Arrange
        number = 5
        expected = 25

        # Act
        result = self.tested_function(number)

        # Assert
        self.assertEqual(result, expected)

    def test_negative_number(self):
        # Arrange
        number = -7
        expected = 49

        # Act
        result = self.tested_function(number)

        # Assert
        self.assertEqual(result, expected)

    def test_zero(self):
        # Arrange
        number = 0
        expected = 0

        # Act
        result = self.tested_function(number)

        # Assert
        self.assertEqual(result, expected)

# python -m unittest
# OR python path-to-file.py
if __name__ == '__main__':
     unittest.main(verbosity=2)
