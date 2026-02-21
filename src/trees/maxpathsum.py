from src.trees.utils import TreeNode
from collections import defaultdict
import math

"""
Return the maximum sum of a continuous path in a binary tree. A path is defined by the following characteristics:

Consists of a sequence of nodes that can begin and end at any node in the tree
Each consecutive pair of nodes in the sequence is connected by an edge
The path must be a single continuous sequence of nodes that doesn't split into multiple paths
"""

def max_path_sum(root: TreeNode) -> int:
    nodeMaxDown, parents = defaultdict(lambda: -math.inf), {}
    leafs = []
    parents[id(root)] = None

    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        if not current.left and not current.right:
            leafs.append(current)
        if current.right:
            parents[id(current.right)] = current
            stack.append(current.right)
        if current.left:
            parents[id(current.left)] = current
            stack.append(current.left)

    # For “gain” DP it’s more natural that missing child contributes 0 (not -inf)
    nodeMaxDown[id(None)] = 0
    currentMax = -math.inf

    for leaf in leafs:
        current = leaf
        while current:
            leftGain = max(0, nodeMaxDown[id(current.left)])
            rightGain = max(0, nodeMaxDown[id(current.right)])

            # candidate that may use BOTH sides (do not pass upward)
            withBoth = current.val + leftGain + rightGain
            currentMax = max(currentMax, withBoth)

            # downward gain passed to parent (ONE side max)
            nodeMaxDown[id(current)] = current.val + max(leftGain, rightGain)

            current = parents[id(current)]

    return currentMax
