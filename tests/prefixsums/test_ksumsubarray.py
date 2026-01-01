import unittest
from src.prefixsums.ksumsubarray import k_sum_subarrays

class TestKSumSubarray(unittest.TestCase):

    def test_k_sum_subarray(self):
        self.assertEqual(k_sum_subarrays([0, 0, 0, 0, 0], 0), 15)
        self.assertEqual(k_sum_subarrays([], 0), 0)
        self.assertEqual(k_sum_subarrays([1, 2, -1, 1, 2], 3), 3)
        self.assertEqual(k_sum_subarrays([1,-1,1,-1,1], 0), 6)
