from src.linkedlist.utils import ListNode

def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    point_A, point_B = head_A, head_B
    while point_A != point_B:
        point_A = point_A.next if point_A else head_B
        point_B = point_B.next if point_B else head_A
    return point_A
