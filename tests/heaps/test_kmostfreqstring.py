import unittest
from src.heaps.kmostfreqstring import k_most_frequent_strings

class TestKMostFrequentStrings(unittest.TestCase):

    def test_k_most_frequent_strings(self):
        self.assertEqual(k_most_frequent_strings(['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], 2),
                         ['go', 'byte'])
        self.assertEqual(k_most_frequent_strings([], 2), [])        
        self.assertEqual(k_most_frequent_strings(['go', 'go', 'go'], 1), ['go'])                