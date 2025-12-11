import unittest
from src.binarysearch.findinsertionindex import find_the_insertion_index

class TestFindInsertionIndex(unittest.TestCase):

    def test_find_the_insertion_index(self):
        self.assertEqual(find_the_insertion_index([1, 2, 4, 5, 7, 8, 9], 4), 2)
        self.assertEqual(find_the_insertion_index([1, 2], 0), 0)
        self.assertEqual(find_the_insertion_index([1, 2], 3), 2)
        self.assertEqual(find_the_insertion_index([], 3), 0)
        self.assertEqual(find_the_insertion_index([0, 2], 1), 1)