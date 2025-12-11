import unittest
from src.hashmaps.longestchaincn import longest_chain_of_consecutive_numbers

class TestLongestChainOfConsecutiveNumbers(unittest.TestCase):

    def test_longest_chain_of_consecutive_numbers(self):
        self.assertEqual(longest_chain_of_consecutive_numbers([1, 6, 2, 5, 8, 7, 10, 3]), 4)