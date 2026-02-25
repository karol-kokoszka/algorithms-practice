import unittest
from src.graphs.deepcopy import graph_deep_copy
from src.graphs.utils import GraphNode

class TestDeepCopy(unittest.TestCase):

    def test_deep_copy(self):
        graph = [GraphNode(0), GraphNode(1), GraphNode(2), GraphNode(3)]
        graph[0].neighbors = [graph[1], graph[2]]
        graph[1].neighbors = [graph[0], graph[2]]
        graph[2].neighbors = [graph[0], graph[1], graph[3]]
        graph[3].neighbors = [graph[2]]

        self.assertEqual(graph[0].equals_unordered_by_val(graph_deep_copy(graph[0])), True)