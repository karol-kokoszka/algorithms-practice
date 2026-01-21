from src.trees.utils import TreeNode
from typing import List, Tuple
from collections import deque

def rightmost_nodes_of_a_binary_tree(root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []
    q = deque()
    q.append((root, 0))
    
    while q:
        current = q.popleft()
        if not q:
            result.append(current[0].val)
        elif q[0][1] > current[1]:
            result.append(current[0].val)

        if current[0].left:
            q.append((current[0].left, current[1] + 1))
        if current[0].right:
            q.append((current[0].right, current[1] + 1))

    return result