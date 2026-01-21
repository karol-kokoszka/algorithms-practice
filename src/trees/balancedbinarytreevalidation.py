from src.trees.utils import TreeNode
from typing import Tuple

def maxHeight(node: TreeNode) -> Tuple[int, bool]:
    if not node:
        return 0, True
    left = maxHeight(node.left)
    if not left[1]:
        return 0, False
    right = maxHeight(node.right)
    if not right[1]:
        return 0, False
    if abs(left[0] - right[0]) > 1:
        return 0, False
    
    return 1 + max(left[0], right[0]), True


def balanced_binary_tree_validation(root: TreeNode) -> bool:
    return maxHeight(root)[1]