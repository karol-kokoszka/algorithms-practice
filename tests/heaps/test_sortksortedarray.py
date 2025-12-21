import unittest
from src.heaps.sortksortedarray import sort_a_k_sorted_array

class TestSortKSortedArray(unittest.TestCase):

    def test_sort_a_k_sorted_array(self):
        self.assertEqual(sort_a_k_sorted_array([5, 1, 9, 4, 7, 10], 2), [1, 4, 5, 7, 9, 10])
        self.assertEqual(sort_a_k_sorted_array([5, 1, 9, 4], 2), [1, 4, 5, 9])
