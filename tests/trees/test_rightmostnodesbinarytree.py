import unittest
from src.trees.utils import TreeNode
from src.trees.rightmostnodesbinarytree import rightmost_nodes_of_a_binary_tree

class TestRightMostNodesBinaryTree(unittest.TestCase):

    def test_right_most_nodes_of_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.right.right = TreeNode(11)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.right.left = TreeNode(6)
        self.assertEqual(rightmost_nodes_of_a_binary_tree(root), [1, 3, 6, 11])

        root = TreeNode(1)
        self.assertEqual(rightmost_nodes_of_a_binary_tree(root), [1])

        root = None
        self.assertEqual(rightmost_nodes_of_a_binary_tree(root), [])