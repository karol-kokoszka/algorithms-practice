import unittest
from src.trees.utils import TreeNode
from src.trees.widestbinarytreelevel import widest_binary_tree_level

class TestWidestBinaryTreeLevel(unittest.TestCase):

    def test_widest_binary_tree_level(self):
        tree = TreeNode(slice=[1,2,3,4,5,None,7,8,9,None,11,None,None,14])
        self.assertEqual(widest_binary_tree_level(tree), 7)

        self.assertEqual(widest_binary_tree_level(None), 0)

        tree = TreeNode(slice=[1,2,3,None,5,6,7,None,None,8,9])
        self.assertEqual(widest_binary_tree_level(tree), 3)
        