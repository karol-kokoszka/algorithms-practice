import unittest
from src.binarysearch.cuttingwood import cutting_wood

class TestCuttingWood(unittest.TestCase):

    def test_cutting_wood(self):
        self.assertEqual(cutting_wood([2, 6, 3, 8], 7), 3)