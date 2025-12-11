import unittest
from src.heaps.combinesortell import combine_sorted_linked_lists
from src.linkedlist.utils import list_node_from_array

class TestCombineSortedLinkedList(unittest.TestCase):

    def test_combine_sorted_linked_list(self):
        l1 = list_node_from_array([1, 6])
        l2 = list_node_from_array([1, 4, 6])
        l3 = list_node_from_array([3, 7])
        l4 = list_node_from_array([1, 1, 3, 4, 6, 6, 7])

        result = combine_sorted_linked_lists([l1, l2, l3, l4])
        print(result)