import unittest
from src.graphs.shortesttranformationsequence import shortest_transformation_sequence

class TestShortestTransformationSequence(unittest.TestCase):

    def test_shortest_transformation_sequence(self):
        self.assertEqual(shortest_transformation_sequence("red", "hit", [
            'red', 'bed', 'hat', 'rod', 'rad', 'rat', 'hit', 'bad', 'bat'
        ]), 5)
        self.assertEqual(shortest_transformation_sequence("red", "red", [
            'red', 'bed', 'hat', 'rod', 'rad', 'rat', 'hit', 'bad', 'bat'
        ]), 1)
        self.assertEqual(shortest_transformation_sequence("red", "red", []), 0)       
