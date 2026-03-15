import unittest
from src.backtracking.findallsubsets import find_all_subsets

class TestFindAllSubsets(unittest.TestCase):

    def test_find_all_subsets(self):
        self.assertCountEqual(find_all_subsets([4, 5, 6]), [[], [4], [4, 5], [4, 5, 6], [4, 6], [5], [5, 6], [6]])
        self.assertCountEqual(find_all_subsets([]), [[]])
        self.assertCountEqual(find_all_subsets([4]), [[], [4]])