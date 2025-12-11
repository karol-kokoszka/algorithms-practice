from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    matchTarget = {}
    i = 0
    while i < len(nums):
        if (match := matchTarget.get(nums[i])) is not None:
            return [match, i]
        matchTarget[target - nums[i]] = i
        i = i + 1
    return []