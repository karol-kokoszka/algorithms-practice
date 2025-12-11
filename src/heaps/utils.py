from typing import Callable, List, Generic, TypeVar

T = TypeVar("T")

"""
HeapImpl is the generic implementation of heap.
Requires 'compare' function to be passed to the constructor which contract states:
- returns 0 -> equal
- returns -1 -> first argument has lower priority
- returns 1 -> first argument has higher priority 
"""
class HeapImpl(Generic[T]):

    __slots__ = ("data", "compare")

    def __init__(self, compare: Callable[[T, T], int], data: List[T] = None, build: bool = False):
        self.data: List[T] = data if data != None else []
        self.compare: Callable[[T, T], int] = compare
        if build:
            self.build_heap()

    def parent(self, idx: int) -> int:
        return (idx - 1) // 2
    
    def left(self, idx: int) -> int:
        return 2 * idx + 1
    
    def right(self, idx: int) -> int:
        return 2 * idx + 2
    
    def insert(self, value: T) -> None:
        self.data.append(value)
        self.shift_up(len(self.data) - 1)

    def build_heap(self) -> None:
        idx = len(self.data) // 2 - 1
        while idx >= 0:
            self.shift_down(idx)
            idx -= 1

    def shift_up(self, idx: int) -> None:
        # as long as elem[idx] has higher prio than parent, replace positions
        while idx != 0 and self.compare(self.data[idx], self.data[self.parent(idx)]) == 1:
            parentIdx = self.parent(idx)
            self.data[idx], self.data[parentIdx] = self.data[parentIdx], self.data[idx]
            idx = parentIdx      
   
    def shift_down(self, idx: int) -> None:
        lastIdx = len(self.data) - 1
        while self.left(idx) <= lastIdx:
            leftIdx, rightIdx = self.left(idx), self.right(idx)
            replaceIdx = rightIdx
            if rightIdx > lastIdx or self.compare(self.data[leftIdx], self.data[rightIdx]) == 1:
                replaceIdx = leftIdx                
            if self.compare(self.data[replaceIdx], self.data[idx]) == 1:
                self.data[replaceIdx], self.data[idx] = self.data[idx], self.data[replaceIdx]
            else:
                return
            idx = replaceIdx
    
    def extract_max(self) -> T:
        if len(self.data) == 0:
            return None
        max = self.data[0]
        temp = self.data.pop()
        if len(self.data) > 0:
            self.data[0] = temp
            self.shift_down(0)
        return max
    
    def pushList(self, elements: List[T]) -> None:
        self.data = self.data + elements
        self.build_heap()
        
