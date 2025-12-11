from typing import List

def find_the_target_in_a_rotated_sorted_array(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        # sorted right part
        if nums[mid] < nums[right]:
            if nums[mid] < target:
                if nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid
            else:
                right = mid
        # sorted left part
        else:
            if nums[mid] >= target:
                if nums[left] > target:
                    left = mid + 1
                else:
                    right = mid
            else:
                left = mid + 1
    return left if nums[left] == target else -1

# [4, 5, 1, 2, 3], 3)
# 4 5 1 2 3 
# ---------
# 0 1 2 3 4