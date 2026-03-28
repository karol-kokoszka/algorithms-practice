import unittest
from src.dynamic.longestcommonsubsequence import longest_common_subsequence

class TestLongestCommonSubsequnce(unittest.TestCase):

    def test_longest_common_subsequnce(self):
        self.assertEqual(longest_common_subsequence('aebab', 'acabac'), 3)
        self.assertEqual(longest_common_subsequence('acabac', 'aebab'), 3)
        self.assertEqual(longest_common_subsequence('', 'acabac'), 0)        
        self.assertEqual(longest_common_subsequence('asdasd', ''), 0)        
        self.assertEqual(longest_common_subsequence('abcdefg', 'bdfp'), 3)
