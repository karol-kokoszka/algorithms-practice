import unittest
from src.dynamic.mincoincombination import min_coin_combination

class TestMinCoinCombination(unittest.TestCase):

    def test_min_coin_combination(self):
        self.assertEqual(min_coin_combination(coins = [1, 2, 3], target = 5), 2)
        self.assertEqual(min_coin_combination(coins = [4, 5], target = 6), -1)