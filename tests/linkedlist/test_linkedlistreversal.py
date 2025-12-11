import unittest
from typing import List
from src.linkedlist.linkedlistreversal import linked_list_reversal, linked_list_reversal_recursive
from src.linkedlist.utils import ListNode, list_node_from_array

class TestLinkedListReversal(unittest.TestCase):

    def test_linked_list_reversal(self):
        input = list_node_from_array([1,2,4,7,3])
        output = linked_list_reversal(input)
        expected = list_node_from_array([3,7,4,2,1])
        self.assertEqual(output, expected)

    def test_linked_list_reversal_recursive(self):
        input = list_node_from_array([1,2,4,7,3])
        output = linked_list_reversal_recursive(input)
        expected = list_node_from_array([3,7,4,2,1])
        self.assertEqual(output, expected)
