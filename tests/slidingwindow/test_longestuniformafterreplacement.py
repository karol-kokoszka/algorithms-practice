import unittest
from src.slidingwindow.longestuniformafterreplacement import longest_uniform_substring_after_replacements

class TestLongestUniformStringAfterReplacement(unittest.TestCase):

    def test_longest_uniform_string_after_replacement(self):
        self.assertEqual(longest_uniform_substring_after_replacements('AABCDCCA', 2), 5)
        self.assertEqual(longest_uniform_substring_after_replacements('aaaa', 2), 4)
        self.assertEqual(longest_uniform_substring_after_replacements('aaaa', 0), 4)
        self.assertEqual(longest_uniform_substring_after_replacements('', 0), 0)