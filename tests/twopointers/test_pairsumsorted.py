import unittest
from src.twopointers.pairsumsorted import pair_sum_sorted

class TestPairSumSorted(unittest.TestCase):

    def test_pair_sum_sorted(self):
        self.assertEqual(pair_sum_sorted([1, 2, 3, 4, 6], 6), [1, 3])

if __name__ == '__main__':
    unittest.main()