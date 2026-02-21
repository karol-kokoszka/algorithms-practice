import unittest
from src.trees.maxpathsum import max_path_sum
from src.trees.utils import TreeNode

class TestMaxPathSum(unittest.TestCase):

    def test_max_path_sum(self):
        root = TreeNode(slice=[5, -10, 8, 1, -7, 9, 7, 11, None, -1, None, None, None, 6, -3])
        self.assertEqual(max_path_sum(root), 30)

    def test_max_path_sum_single_node_positive(self):
        root = TreeNode(slice=[7])
        self.assertEqual(max_path_sum(root), 7)

    def test_max_path_sum_single_node_negative(self):
        root = TreeNode(slice=[-7])
        self.assertEqual(max_path_sum(root), -7)

    def test_max_path_sum_two_levels_choose_best_child(self):
        #      1
        #     / \
        #    2   3
        # max path: 2 -> 1 -> 3 = 6
        root = TreeNode(slice=[1, 2, 3])
        self.assertEqual(max_path_sum(root), 6)

    def test_max_path_sum_all_negative(self):
        #      -10
        #      /  \
        #    -20  -30
        # max path should be the least negative single node: -10
        root = TreeNode(slice=[-10, -20, -30])
        self.assertEqual(max_path_sum(root), -10)

    def test_max_path_sum_max_path_not_through_root(self):
        #      -10
        #      /  \
        #     9   20
        #         / \
        #        15  7
        # max path: 15 -> 20 -> 7 = 42
        root = TreeNode(slice=[-10, 9, 20, None, None, 15, 7])
        self.assertEqual(max_path_sum(root), 42)

    def test_max_path_sum_requires_ignoring_negative_branches(self):
        #      2
        #     / \
        #   -1   3
        # max path: 2 -> 3 = 5 (ignore -1)
        root = TreeNode(slice=[2, -1, 3])
        self.assertEqual(max_path_sum(root), 5)

    def test_max_path_sum_right_skewed(self):
        # 1 -> 2 -> 3 -> 4
        # max path: 1+2+3+4 = 10
        root = TreeNode(slice=[1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
        self.assertEqual(max_path_sum(root), 10)

    def test_max_path_sum_left_skewed_with_negatives(self):
        #    5
        #   /
        # -2
        # /
        # 3
        # max path: 5 + (-2) + 3 = 6 (continuous path)
        root = TreeNode(slice=[5, -2, None, 3])
        self.assertEqual(max_path_sum(root), 6)

    def test_max_path_sum_mixed_with_gaps(self):
        #        1
        #       / \
        #      2   3
        #       \
        #        4
        # max path: 4 -> 2 -> 1 -> 3 = 10
        root = TreeNode(slice=[1, 2, 3, None, 4])
        self.assertEqual(max_path_sum(root), 10)