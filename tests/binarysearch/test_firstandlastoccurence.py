import unittest
from src.binarysearch.firstandlastoccurence import first_and_last_occurrences_of_a_number

class TestFirstAndLastOccurrences(unittest.TestCase):

    def test_first_and_last_occurrences(self):
        self.assertEqual(first_and_last_occurrences_of_a_number([1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], 4), [3, 5])
        self.assertEqual(first_and_last_occurrences_of_a_number([1, 2, 4], 3), [-1, -1])
        self.assertEqual(first_and_last_occurrences_of_a_number([1,2,3,4,5,6,7,8,9,10], 11), [-1, -1])