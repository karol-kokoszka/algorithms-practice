import unittest
from src.slidingwindow.longestuniquesubstring import longest_substring_with_unique_chars

class TestLongestUniqueSubstring(unittest.TestCase):

    def test_longest_substring_with_unique_chars(self):
        self.assertEqual(longest_substring_with_unique_chars('abcba'), 3)
        self.assertEqual(longest_substring_with_unique_chars(''), 0) 
        self.assertEqual(longest_substring_with_unique_chars('aaaaaaa'), 1)    
        self.assertEqual(longest_substring_with_unique_chars('aaaaaabcbc'), 3)           
        self.assertEqual(longest_substring_with_unique_chars('abc'), 3)           