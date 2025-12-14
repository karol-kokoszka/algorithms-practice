from typing import List, Optional

class MultiLevelListNode:
    def __init__(self, val=None, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Node:
    __slots__ = ("val", "key", "prev", "next")
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None  

    def prepend(self, elem, key) -> None:
        if self.head is None:
            self.head = Node(elem, key)
            self.tail = self.head
            return
        newHead = Node(elem, key)
        newHead.next = self.head
        self.head.prev = newHead
        self.head = newHead

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values) + " H" + str(self.head.val) + " T" + str(self.tail.val)

    def printReverse(self):
        values = []
        current = self.tail
        while current:
            values.append(str(current.val))
            current = current.prev
        print(" -> ".join(values))


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)
    
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next

        return a is None and b is None
    
def list_node_from_array(array: List[int]) -> ListNode:
    if len(array) == 0:
        return None
    head = ListNode(array[0])
    curr = head
    for i in range(1, len(array)):
        curr.next = ListNode(array[i])
        curr = curr.next
    return head

class MultiLevelListNode:
    def __init__(self, val=None, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


def from_array_to_multi_level_list_node(data):
    """
    Build a multi-level list from an array where each node is:
      - [val]                  -> no child
      - [val, children_list]   -> has child

    children_list uses the same structure.
    """
    if not data:
        return None

    head = None
    prev = None

    for entry in data:
        # Validate entry
        if not isinstance(entry, (list, tuple)) or len(entry) not in (1, 2):
            raise ValueError(f"Invalid node entry: {entry!r} (expected [val] or [val, children])")

        val = entry[0]
        children = entry[1] if len(entry) == 2 else None

        # If children is provided, it must be a list (the child list)
        if children is not None and not isinstance(children, (list, tuple)):
            raise ValueError(f"Children must be a list for node {val!r}, got {type(children).__name__}")

        node = MultiLevelListNode(val)

        if prev:
            prev.next = node
        else:
            head = node

        if children:
            node.child = from_array_to_multi_level_list_node(children)

        prev = node

    return head


def from_multi_level_list_node_to_array(head):
    """
    Serialize a multi-level list back to the short form:
      - [val] if no child
      - [val, children_list] if child exists
    """
    result = []
    curr = head
    while curr:
        if curr.child:
            child_arr = from_multi_level_list_node_to_array(curr.child)
            result.append([curr.val, child_arr])
        else:
            result.append([curr.val])
        curr = curr.next
    return result