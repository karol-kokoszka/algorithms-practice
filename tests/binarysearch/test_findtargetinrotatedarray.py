import unittest
from src.binarysearch.findtargetinrotatedarray import find_the_target_in_a_rotated_sorted_array

class TestFindTargetInARotatedArray(unittest.TestCase):

    def test_find_the_target_in_a_rotated_array(self):
        self.assertEqual(find_the_target_in_a_rotated_sorted_array([4, 5, 1, 2, 3], 1), 2)
        self.assertEqual(find_the_target_in_a_rotated_sorted_array([4, 5, 1, 2, 3], 2), 3)
        self.assertEqual(find_the_target_in_a_rotated_sorted_array([4, 5, 1, 2, 3], 3), 4)
        self.assertEqual(find_the_target_in_a_rotated_sorted_array([4, 5, 1, 2, 3], 4), 0)
        self.assertEqual(find_the_target_in_a_rotated_sorted_array([4, 5, 1, 2, 3], 5), 1)
        self.assertEqual(find_the_target_in_a_rotated_sorted_array([], 1), -1)
