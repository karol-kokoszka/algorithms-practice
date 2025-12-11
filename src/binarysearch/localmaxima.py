from typing import List

"""
A local maxima is a value greater than both its immediate neighbors.
Return any local maxima in an array. You may assume that an element is always considered
to be strictly greater than a neighbor that is outside the array.
"""
def local_maxima_in_array(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        raise ValueError("Array must be non-empty")

    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2

        # Compare mid with its right neighbor.
        # If nums[mid] < nums[mid + 1], then there must be a peak on the right.
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            # nums[mid] >= nums[mid + 1], so there must be a peak on the left (including mid).
            right = mid

    # left == right, and this index is a local maximum
    return left
