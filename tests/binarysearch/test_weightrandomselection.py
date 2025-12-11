import unittest
from src.binarysearch.weightrandomselection import WeightedRandomSelection

class TestWeightedRandomSelection(unittest.TestCase):

    def test_select(self):
        wrs = WeightedRandomSelection([3, 1, 2, 4])
        selected = 0
        for i in range(10000):
            if wrs.select() == 0:
                selected = selected + 1
        self.assertAlmostEqual(selected, 3000, delta=200)