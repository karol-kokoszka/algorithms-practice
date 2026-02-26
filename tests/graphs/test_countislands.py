import unittest
from src.graphs.countislands import count_islands

class TestCountIslands(unittest.TestCase):

    def test_count_islands(self):
        self.assertEqual(count_islands([[1, 1, 0, 0],[1, 1, 0, 0],[0, 0, 1, 1],[0, 0, 0, 1]]), 2)
        self.assertEqual(count_islands([[1]]), 1)
        self.assertEqual(count_islands([[1,1,0,1],[0,0,1,0],[1,0,0,1],[1,1,1,0],[0,0,0,1]]), 6)

