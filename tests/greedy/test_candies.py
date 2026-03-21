import unittest
from src.greedy.candies import candies

class TestCandies(unittest.TestCase):

    def test_candies(self):
        # self.assertEqual(candies([4, 3, 2, 4, 5, 1]), 12)
        # self.assertEqual(candies([]), 0)
        self.assertEqual(candies([1, 3, 4, 6, 8]), 15)
