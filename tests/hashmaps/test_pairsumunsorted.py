import unittest
from src.hashmaps.pairsumunsorted import pair_sum_unsorted

class TestPairSumUnsorted(unittest.TestCase):

    def test_pairsumunsorted(self):
        self.assertEqual(pair_sum_unsorted([-1, 3, 4, 2], 3), [0, 2])