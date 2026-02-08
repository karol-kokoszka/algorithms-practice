from src.trees.utils import TreeNode

# Return the lowest common ancestor (LCA) of two nodes, p and q, in a binary tree.
# The LCA is defined as the lowest node that has both p and q as descendants. 
# A node can be considered an ancestor of itself.
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    stack = []
    parents = {}
    levels = {}

    stack.append(root)
    parents[id(root)] = None
    levels[id(root)] = 0

    foundP, foundQ = False, False

    # build backtrace metadata and tree-level metadata
    while stack or (not foundP or not foundQ):
        current = stack.pop()
        if current.val == p.val:
            foundP = True
        if current.val == q.val:
            foundQ = True
        if current.right:
            stack.append(current.right)
            parents[id(current.right)] = current
            levels[id(current.right)] = levels[id(current)] + 1
        if current.left:
            stack.append(current.left)
            parents[id(current.left)] = current 
            levels[id(current.left)] = levels[id(current)] + 1

    # fit the tree levels for p and q
    levelP, levelQ = levels[id(p)], levels[id(q)]
    pointerP, pointerQ = p, q
    while levelP != levelQ:
        if levelP > levelQ:
            pointerP = parents[id(pointerP)]
            levelP -= 1
        if levelQ > levelP:
            pointerQ = parents[id(pointerQ)]
            levelQ -= 1

    # find LCA
    while pointerP.val != pointerQ.val:
        pointerP = parents[id(pointerP)]
        pointerQ = parents[id(pointerQ)]

    return pointerP
