import unittest
from src.fastandslowpointers.happynumber import happy_number, square_digits_and_sum

class TestHappyNumber(unittest.TestCase):

    def test_happy_number(self):
        self.assertEqual(happy_number(23), True)
        self.assertEqual(happy_number(1), True)
        self.assertEqual(happy_number(2), False)

    def test_square_digits_and_sum(self):
        self.assertEqual(square_digits_and_sum(10), 1)
        self.assertEqual(square_digits_and_sum(23), 13)