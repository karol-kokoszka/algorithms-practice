import unittest
from src.dynamic.climbingstairs import climbing_stairs

class TestClimbingStairs(unittest.TestCase):

    def test_climbing_stairs(self):
        self.assertEqual(climbing_stairs(4), 5)
        self.assertEqual(climbing_stairs(0), 0)