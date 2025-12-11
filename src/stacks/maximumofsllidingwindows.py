from typing import List
from collections import deque

def maximums_of_sliding_window(nums: List[int], k: int) -> List[int]:
    if k == 0 or len(nums) == 0 or k > len(nums):
        return []
    candidates = deque()
    output = []
    i = 0
    while i < len(nums) and i < k:
        while candidates and candidates[-1][0] <= nums[i]:
            candidates.pop()
        candidates.append((nums[i], i))
        i += 1
    left, right = 0, k - 1 
    while right < len(nums):
        if candidates[0][1] < left:
            candidates.popleft()
        output.append(candidates[0][0])
        left += 1
        right += 1
        if right < len(nums):
            while candidates and candidates[-1][0] <= nums[right]:
                candidates.pop()
            candidates.append((nums[right], right))
    return output