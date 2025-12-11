import unittest
from src.fastandslowpointers.linkedlistloops import linked_list_loop
from src.linkedlist.utils import list_node_from_array

class TestLinkedLinkLoops(unittest.TestCase):

    def test_linked_link_loops(self):
        withCycle = list_node_from_array([0,1,2,3,4,5])
        cur = withCycle
        cycle = None
        while cur.val != 5:
            if cur.val == 2:
                cycle = cur
            cur = cur.next
        cur.next = cycle

        self.assertEqual(linked_list_loop(withCycle), True)
        self.assertEqual(linked_list_loop(list_node_from_array([0,1,2,3,4,5])), False)