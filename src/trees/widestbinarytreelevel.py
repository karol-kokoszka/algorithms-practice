from src.trees.utils import TreeNode

def widest_binary_tree_level(root: TreeNode) -> int:
    currentLevel = [root]
    size = 0
    while currentLevel:
        nextLevel = []
        leftMost, rightMost = 0, 0
        while leftMost < len(currentLevel) and currentLevel[leftMost] == None:
            leftMost+=1
        if leftMost >= len(currentLevel):
            return size
        for i in range(leftMost, len(currentLevel)):
            if currentLevel[i] == None:
                nextLevel.append(None)
                nextLevel.append(None)
            else:
                rightMost = max(rightMost, i)
                nextLevel.append(currentLevel[i].left)
                nextLevel.append(currentLevel[i].right)
        size = max(size, rightMost + 1 - leftMost)
        currentLevel = nextLevel 
    return size