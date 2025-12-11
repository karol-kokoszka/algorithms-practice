from src.linkedlist.utils import ListNode

def linked_list_loop(head: ListNode) -> bool:
    fastPointer = head
    slowPointer = head
    
    while fastPointer:
        slowPointer = slowPointer.next
        if fastPointer.next:
            fastPointer = fastPointer.next.next
        else:
            return False
        if fastPointer and slowPointer.val == fastPointer.val:
            return True
    return False