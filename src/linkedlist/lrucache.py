from src.linkedlist.utils import DoublyLinkedList, Node
from typing import Dict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.used: int = 0
        self.map: Dict[int, Node] = {}
        self.lru: DoublyLinkedList = DoublyLinkedList()
        pass

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node:
            # move the element to the beginning of LRU
            if node.prev:
                node.prev.next = node.next
            else:
                self.lru.head = node.next

            if node.next:
                node.next.prev = node.prev
            else:
                self.lru.tail = node.prev

            self.lru.prepend(node.val, key)
            self.map[key] = self.lru.head

        return -1 if node is None else node.val

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node != None:
            # move the element to the beginning of LRU
            # and assign new value
            if node.prev != None:
                node.prev.next = node.next
                self.lru.prepend(value, key)
                self.map[key] = self.lru.head
        else:
            # add element to the beginning of LRU
            # remove last element from LRU if capacity is exceeded
            # add reference to map
            self.used += 1
            if self.used > self.capacity:
                self.used = self.capacity
                del self.map[self.lru.tail.key]
                self.lru.tail.prev.next = None
                self.lru.tail = self.lru.tail.prev
            self.lru.prepend(value, key)
            self.map[key] = self.lru.head
