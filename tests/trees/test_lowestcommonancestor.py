import unittest
from src.trees.utils import TreeNode
from src.trees.lowestcommonancestor import lowest_common_ancestor

class TestLowestCommonAncestor(unittest.TestCase):

    def test_lowest_common_ancestor(self):
        root = TreeNode(slice=[1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9])
        self.assertEqual(lowest_common_ancestor(root, root.right.right, root.right.left.left), root.right)
        root = TreeNode(slice=[20, 10, 30, 5, 15, 25, 35, None, None, 13, 17])
        self.assertEqual(lowest_common_ancestor(root, root.left, root.left.right.right), root.left)        