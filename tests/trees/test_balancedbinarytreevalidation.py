import unittest
from src.trees.balancedbinarytreevalidation import balanced_binary_tree_validation
from src.trees.utils import TreeNode

class TestBalancedBinaryTreeValidation(unittest.TestCase):

    def test_balanced_binary_tree_validation(self):
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.right.right = TreeNode(9)
        root.right.right.left = TreeNode(6)
        self.assertEqual(balanced_binary_tree_validation(root), False)

