import unittest
from src.prefixsums.sumbetweenrange import SumBetweenRange

class TestSumBetweenRange(unittest.TestCase):

    def test_sum_between_range(self):
        s = SumBetweenRange([3, -7, 6, 0, -2, 5])
        self.assertEqual(s.sum_range(0, 3), 2)
        self.assertEqual(s.sum_range(2, 4), 4)
        self.assertEqual(s.sum_range(2, 2), 6)        