from typing import List

# You are given a sorted array that contains unique values, along with an integer target.
# If the array contains the target value, return its index.
# Otherwise, return the insertion index. This is the index
# where the target would be if it were inserted in order,
# maintaining the sorted sequence of the array.
def find_the_insertion_index(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid  
    return left