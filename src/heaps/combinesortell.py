from typing import List
from src.linkedlist.utils import ListNode
from src.heaps.utils import HeapImpl

def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    def compare(a: ListNode, b: ListNode) -> int:
        if a.val < b.val:
            return 1
        if a.val > b.val:
            return -1
        return 0
    
    tops = HeapImpl(compare=compare)
    head = ListNode()
    current = head
    currentList = lists
    
    while currentList:
        newList = []
        currentTops = []
        for list in currentList:
            if list:
                if list.next:
                    tmp = list.next
                    newList.append(tmp)
                list.next = None
                currentTops.append(list)
        tops.pushList(currentTops)
        currentList = newList
        current.next = tops.extract_max()
        current = current.next
    
    top = tops.extract_max()
    while top:
        current.next = top
        current = current.next
        top = tops.extract_max()
    
    return head.next 

    
        