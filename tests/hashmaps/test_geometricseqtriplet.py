import unittest
from src.hashmaps.geometricseqtriplet import geometric_sequence_triplets

class TestGeometricSequenceTriplet(unittest.TestCase):

    def test_geometric_sequence_triplet(self):
        self.assertEqual(geometric_sequence_triplets([2, 1, 2, 4, 8, 8], 2), 5)