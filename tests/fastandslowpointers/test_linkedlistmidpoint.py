import unittest
from src.fastandslowpointers.linkedlistmidpoint import linked_list_midpoint
from src.linkedlist.utils import list_node_from_array

class TestLinkedListMidpoint(unittest.TestCase):

    def test_linked_list_midpoint(self):
        testList = list_node_from_array([1,2,4,7])
        self.assertEqual(linked_list_midpoint(testList), testList.next.next)