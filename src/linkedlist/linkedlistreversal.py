from src.linkedlist.utils import ListNode

def linked_list_reversal(head: ListNode) -> ListNode:
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def linked_list_reversal_recursive(head: ListNode) -> ListNode:
    if (not head) or (not head.next):
        return head
    reversedRight = linked_list_reversal_recursive(head.next)
    head.next.next = head
    head.next = None
    return reversedRight

