import unittest
from typing import Callable


class TestAbs(unittest.TestCase):
    def setUp(self) -> None:
        self.tested_function = self._generateTestedFunction()

    @staticmethod
    def _generateTestedFunction() -> Callable[[int], int]:
        from src.abs import my_abs
        return my_abs

    def test_positive_number(self):
        """Test my abs for positive number"""
        self.assertEqual(self.tested_function(5), 5, "Should be 5")

    def test_negative_number(self):
        self.assertEqual(self.tested_function(-10), 10, "Should be 10")

    def test_zero(self):
        self.assertEqual(self.tested_function(0), 0, "Should be 0")


# python -m unittest test_abs.py
if __name__ == '__main__':
    unittest.main(verbosity=2)
