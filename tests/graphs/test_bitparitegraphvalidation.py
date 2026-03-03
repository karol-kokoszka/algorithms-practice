import unittest
from src.graphs.bitparitegraphvalidation import bipartite_graph_validation

class TestBitpariteGraphValidation(unittest.TestCase):
    
    def test_bitpartie_graph_validation(self):
        self.assertEqual(bipartite_graph_validation([[1, 4], [0, 2], [1], [4], [0, 3]]), True)
        self.assertEqual(bipartite_graph_validation([]), True)
        self.assertEqual(bipartite_graph_validation([[1, 2, 4], [0, 2], [1], [4], [0, 3]]), False)
        self.assertEqual(bipartite_graph_validation([[1],[0],[3],[2,4],[3,5],[3,4]]), False)
        self.assertEqual(bipartite_graph_validation([[1],[0],[3],[2]]), True)
