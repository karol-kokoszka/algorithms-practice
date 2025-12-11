import unittest
from src.twopointers.tripletsum import triplet_sum

class TestTripletSum(unittest.TestCase):
    
    def test_triplet_sum(self):
        self.assertEqual(triplet_sum([0, -1, 2, -3, 1]), [[-3, 1, 2], [-1, 0, 1]])
        self.assertEqual(triplet_sum([1,2,-2,-1,0,1,-1]), [[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]])
    
