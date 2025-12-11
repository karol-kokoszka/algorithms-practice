from src.linkedlist.utils import MultiLevelListNode

def flatten_multi_level_list(head: MultiLevelListNode) -> MultiLevelListNode:
    actualLevel = [head]
    newList = MultiLevelListNode()
    listIterator = newList

    i = 0
    nextLevel = []
    while i < len(actualLevel) and actualLevel[i]:
        node = actualLevel[i]
        while node:
            if node.child:
                nextLevel.append(node.child)
            listIterator.next = MultiLevelListNode(node.val)
            listIterator = listIterator.next
            node = node.next
        i += 1
        if i >= len(actualLevel):
            i = 0
            actualLevel = nextLevel
            nextLevel = []
    return newList.next