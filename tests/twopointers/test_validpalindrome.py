import unittest
from src.twopointers.validpalindrome import is_palindrome_valid

class TestValidPalindrome(unittest.TestCase):

    def test_is_valid_palindrome(self):
        self.assertEqual(is_palindrome_valid('a dog! a panic in a pagoda.'), True)
        self.assertEqual(is_palindrome_valid('abcde'), False)
        self.assertEqual(is_palindrome_valid('!@#$%^'), True)  
        self.assertEqual(is_palindrome_valid('!@#a$%^'), True)  
        self.assertEqual(is_palindrome_valid('!@#ab$%^'), False)  