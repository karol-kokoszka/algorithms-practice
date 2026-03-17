import unittest
from src.backtracking.combinationofsumk import combinations_of_sum_k

class TestCombinationOfSumK(unittest.TestCase):

    def test_combination_of_sum_k(self):
        self.assertCountEqual(combinations_of_sum_k([1, 2, 3], 4), [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]])
        self.assertCountEqual(combinations_of_sum_k([1], 0), [[]])
        self.assertCountEqual(combinations_of_sum_k([], 0), [[]])