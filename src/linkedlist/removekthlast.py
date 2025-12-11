from src.linkedlist.utils import ListNode

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    minusK1, minusK = None, None
    curr = head
    i = 0
    while curr and i < k-1:
        curr = curr.next
        i += 1
    if not curr:
        return head
    minusK = head
    while curr.next:
        curr = curr.next
        minusK1 = minusK
        minusK = minusK.next
    if not minusK1:
        return head.next
    minusK1.next = minusK.next
    return head 