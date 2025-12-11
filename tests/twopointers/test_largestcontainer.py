import unittest
from src.twopointers.largestcontainer import largest_container

class TestLargestContainer(unittest.TestCase):

    def test_largest_container(self):
        self.assertEqual(largest_container([2, 7, 8, 3, 7, 6]), 24)