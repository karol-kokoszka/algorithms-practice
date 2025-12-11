import unittest
from src.binarysearch.findmedianfromtwosortedarrays import find_the_median_from_two_sorted_arrays

class TestFindMedianFromTwoSortedArrays(unittest.TestCase):

    def test_find_the_median_from_two_sorted_arrays(self):
        self.assertEqual(find_the_median_from_two_sorted_arrays([0, 2, 5, 6, 8], [1, 3, 7]), 4.0)