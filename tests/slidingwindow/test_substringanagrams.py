import unittest
from src.slidingwindow.substringanagrams import substring_anagrams

class TestSubstringAnagrams(unittest.TestCase):

    def test_substring_anagrams(self):
        self.assertEqual(substring_anagrams('caabab', 'aba'), 2)
        self.assertEqual(substring_anagrams('baa', 'aba'), 1)
        self.assertEqual(substring_anagrams('aaabac', 'a'), 4)
        self.assertEqual(substring_anagrams('anystring', ''), 0)
