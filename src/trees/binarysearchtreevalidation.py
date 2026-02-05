from src.trees.utils import TreeNode

def cmpFn(min: int, max: int, currentV: int) -> bool:
    return (min == None or min < currentV) and (max == None or currentV < max)

def binary_search_tree_validation(root: TreeNode) -> bool:
    return validate_DFS(root, None, None)

def validate_DFS(node: TreeNode, min: int, max: int) -> bool:
    if node == None:
        return True
    if not cmpFn(min, max, node.val):
        return False
    if not validate_DFS(node.left, min, node.val):
        return False
    if not validate_DFS(node.right, node.val, max):
        return False
    return True