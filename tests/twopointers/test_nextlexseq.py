import unittest
from src.twopointers.nextlexseq import next_lexicographical_sequence

class TestNextLexSeq(unittest.TestCase):

    def test_nextLexSeq(self):
        self.assertEqual(next_lexicographical_sequence('abcd'), 'abdc')
        self.assertEqual(next_lexicographical_sequence('adbc'), 'adcb')
        self.assertEqual(next_lexicographical_sequence('dcba'), 'abcd')
        self.assertEqual(next_lexicographical_sequence('cadb'), 'cbad')
        self.assertEqual(next_lexicographical_sequence('a'), 'a')
        self.assertEqual(next_lexicographical_sequence('abcedda'), 'abdacde')

        