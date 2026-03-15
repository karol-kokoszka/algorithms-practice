import unittest
from src.backtracking.findallpermutations import find_all_permutations

class TestFindAllPermutations(unittest.TestCase):

    def test_find_all_permutations(self):
        self.assertEqual(find_all_permutations([4, 5, 6]), [[4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 5, 4], [6, 4, 5]])
        self.assertEqual(find_all_permutations([]), [[]])        
        self.assertEqual(find_all_permutations([1]), [[1]])  