import unittest
from src.trees.utils import TreeNode
from src.trees.binarysearchtreevalidation import binary_search_tree_validation

class TestBinarySearchTreeValidation(unittest.TestCase):

    def test_binary_search_tree_validation(self):
        tree = TreeNode(slice=[5, 2, 7, 1, 6, 7, 9])
        self.assertEqual(binary_search_tree_validation(tree), False)
        tree = TreeNode(slice=[5,3,8,2,4,6,10])
        self.assertEqual(binary_search_tree_validation(tree), True)
        tree = TreeNode(slice=[5,3,8,2,7,6,10])
        self.assertEqual(binary_search_tree_validation(tree), False)        