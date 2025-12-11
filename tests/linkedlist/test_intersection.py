import unittest
from src.linkedlist.intersection import linked_list_intersection
from src.linkedlist.utils import ListNode, list_node_from_array

class TestIntersection(unittest.TestCase):

    def test_intersection(self):
        headA = list_node_from_array([1,3,4,8,7,2])
        headB = list_node_from_array([6,4,8,7,2])
        # need to remove _eq_ from ListNode
        # list must intersect not by value, but one list must contain another list
        # including memory addresses
