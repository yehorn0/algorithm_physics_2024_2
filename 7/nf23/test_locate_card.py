import unittest
from locate_card import locate_card


class LocateCardTestCase(unittest.TestCase):
    def setUp(self):
        self.test_cases = [{
            "in": {
                "cards": [3, 2, 1],
                "query": 2,
            },
            "out": 1
        }, {
            "in": {
                "cards": [13, 12, 11, 7, 4, 3, 1, 0],
                "query": 7,
            },
            "out": 3
        }, {
            "in": {
                "cards": [9, 7, 5, 2, -9],
                "query": 6,
            },
            "out": -1
        }, {
            "in": {
                "cards": [],
                "query": 7,
            },
            "out": -1
        }]

    def test_locate_card(self):
        for case in self.test_cases:
            actual = locate_card(case["in"]["cards"], case["in"]["query"])
            self.assertEqual(case["out"], actual)


if __name__ == '__main__':
    unittest.main()
