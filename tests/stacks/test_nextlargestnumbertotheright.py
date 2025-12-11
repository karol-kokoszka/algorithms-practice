import unittest
from src.stacks.nextlargestnumbertotheright import next_largest_number_to_the_right

class TestNextLargestNumberToTheRight(unittest.TestCase):

    def test_next_largest_number_to_the_right(self):
        self.assertEqual(next_largest_number_to_the_right([5, 2, 4, 6, 1]), [6, 4, 6, -1, -1])
        self.assertEqual(next_largest_number_to_the_right([4, 4, 4, 4, 4]), [-1, -1, -1, -1, -1])