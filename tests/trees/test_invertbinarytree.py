import unittest
from src.trees.utils import TreeNode
from src.trees.invertbinarytree import invert_binary_tree

class TestInvertBinaryTree(unittest.TestCase):

    def test_invert_binary_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(8)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(6)
        root.right.right = TreeNode(4)

        inverted = TreeNode(5)
        inverted.left = TreeNode(8)
        inverted.right = TreeNode(1)
        inverted.left.left = TreeNode(4)
        inverted.right.left = TreeNode(6)
        inverted.right.right = TreeNode(7)

        self.assertEqual(invert_binary_tree(root), inverted)