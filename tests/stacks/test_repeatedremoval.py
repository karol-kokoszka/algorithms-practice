import unittest
from src.stacks.repeatedremoval import repeated_removal_of_adjacent_duplicates

class TestRepeatedRemovalOfAdjacentDuplicates(unittest.TestCase):

    def test_repeated_removal_of_adjacent_duplicates(self):
        self.assertEqual(repeated_removal_of_adjacent_duplicates('aacabba'), 'c')
        self.assertEqual(repeated_removal_of_adjacent_duplicates('aaa'), 'a')
        self.assertEqual(repeated_removal_of_adjacent_duplicates(''), '')
        self.assertEqual(repeated_removal_of_adjacent_duplicates('aaaa'), '')