import unittest
from src.hashmaps.zerostriping import zero_striping

class TestZeroStriping(unittest.TestCase):

    def test_zerostriping(self):
        t = [[1,2,3,4,5],
            [6,0,6,9,10],
            [11,12,13,14,15],
            [16,17,18,19,0]]
        zero_striping(t)
        self.assertEqual(t, 
                         [[1,0,3,4,0],
                          [0,0,0,0,0],
                          [11,0,13,14,0],
                          [0,0,0,0,0]
                         ])