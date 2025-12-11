import unittest
from src.linkedlist.palindromicll import palindromic_linked_list
from src.linkedlist.utils import list_node_from_array

class TestPalindromicLinkedList(unittest.TestCase):

    def test_palindromic_linked_list(self):
        self.assertEqual(palindromic_linked_list(list_node_from_array([1,2,3,2,1])), True)