import unittest
from typing import Callable


class Lab2TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tested_function = self._build_test_function()

    def _build_test_function(self) -> Callable[[list[int]], int]:
        from src.lab_2 import weights_equilibrium
        return weights_equilibrium

    def test_empty_list(self) -> None:
        initial_weights = []
        expected_equilibrium = -1

        actual_equilibrium = self.tested_function(initial_weights)

        self.assertEqual(expected_equilibrium, actual_equilibrium)

    def test_no_equilibrium_6_6_9(self) -> None:
        initial_weights = [6, 6, 9]
        expected_equilibrium = -1

        actual_equilibrium = self.tested_function(initial_weights)

        self.assertEqual(expected_equilibrium, actual_equilibrium)

    def test_equilibrium_43_51_35_4(self) -> None:
        initial_weights = [43, 51, 35, 4]
        expected_equilibrium = 1

        actual_equilibrium = self.tested_function(initial_weights)

        self.assertEqual(expected_equilibrium, actual_equilibrium)

    def test_equilibrium_big_list(self) -> None:
        initial_weights = [19, 25, 5, 42, 38, 8, 34, 16, 14, 8, 47, 42, 4, 20, 23]
        expected_equilibrium = 7

        actual_equilibrium = self.tested_function(initial_weights)

        self.assertEqual(expected_equilibrium, actual_equilibrium)
        
    def test_equilibrium_7_24_3_38(self) -> None:
        initial_weights = [7, 24, 3, 38]
        expected_equilibrium = 2

        actual_equilibrium = self.tested_function(initial_weights)

        self.assertEqual(expected_equilibrium, actual_equilibrium)
        
# python -m unittest tests.test_lab_2