from typing import List
from collections import deque

def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    stack = []
    result = deque([])
    for i in range(len(nums)-1, -1, -1):
        current = nums[i]
        while stack and stack[-1] <= current:
            stack.pop()
        result.appendleft(-1 if not stack else stack[-1])
        stack.append(current)
    return list(result)