from src.trees.utils import TreeNode
from collections import deque

def invert_binary_tree(root: TreeNode) -> TreeNode:
    q = deque()
    if root:
        q.append(root)
    while q:
        current = q.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

    return root