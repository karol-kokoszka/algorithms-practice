import unittest
from src.graphs.shortestpath import shortest_path

class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        self.assertEqual(shortest_path(6,
            edges = [
                [0, 1, 5],
                [0, 2, 3],
                [1, 2, 1],
                [1, 3, 4],
                [2, 3, 4],
                [2, 4, 5],
            ],
            start = 0), [0, 4, 3, 7, 8, -1])
