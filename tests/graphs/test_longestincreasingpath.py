import unittest
from src.graphs.longestincreasingpath import longest_increasing_path

class TestLongestIncreasingPath(unittest.TestCase):

    def test_longest_increasing_path(self):
        self.assertEqual(longest_increasing_path([[1, 5, 8],
                                                  [3, 4, 4], 
                                                  [7, 9, 2]]), 5)
        self.assertEqual(longest_increasing_path([]), 0)
        self.assertEqual(longest_increasing_path([[]]), 0)
        self.assertEqual(longest_increasing_path([[9, 5, 8],
                                                  [3, 4, 4], 
                                                  [7, 9, 2]]), 4)
