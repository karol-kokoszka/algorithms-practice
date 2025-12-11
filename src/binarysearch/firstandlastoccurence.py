from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if left >= len(nums) or nums[left] != target:
        return [-1, -1]
    first = left
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    last = left - 1
    return [first, last]