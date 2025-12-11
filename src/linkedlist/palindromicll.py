from src.linkedlist.utils import ListNode

def palindromic_linked_list(head: ListNode) -> bool:
    if not head:
        return True
    curr = head
    newHead = ListNode(curr.val)
    i = 1
    while curr.next:
        i += 1
        curr = curr.next
        newHead = ListNode(curr.val, newHead)

    curr = head
    revCurr = newHead
    for _ in range(i // 2):
        if curr.val != revCurr.val:
            return False
        curr = curr.next
        revCurr = revCurr.next

    return True