import unittest
from src.linkedlist.removekthlast import remove_kth_last_node
from src.linkedlist.utils import ListNode, list_node_from_array

class TestRemoveKthLastNode(unittest.TestCase):

    def test_remove_kth_last_node(self):
        input = list_node_from_array([1,2,4,7,3])
        output = remove_kth_last_node(input, 2)
        expected = list_node_from_array([1,2,4,3])
        self.assertEqual(output, expected)

        input = list_node_from_array([1,2,4,7,3])
        output = remove_kth_last_node(input, 1)
        expected = list_node_from_array([1,2,4,7])
        self.assertEqual(output, expected)

        input = list_node_from_array([1,2,4,7,3])
        output = remove_kth_last_node(input, 5)
        expected = list_node_from_array([2,4,7,3])
        self.assertEqual(output, expected)