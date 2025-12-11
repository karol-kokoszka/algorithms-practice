from src.linkedlist.utils import ListNode

def linked_list_midpoint(head: ListNode) -> ListNode:
    slowP = head
    fastP = head
    while fastP:
        if fastP.next:
            fastP = fastP.next.next
        else:
            return slowP
        slowP = slowP.next
    return slowP
    