from typing import List

"""
You are given an integer array in which you're originally positioned at index 0. 
Each number in the array represents the maximum jump distance from the current index. 
Determine if it's possible to reach the end of the array.
"""
def jump_to_the_end(nums: List[int]) -> bool:
    far = 0
    for i in range(len(nums)):
        if far < i:
            return False
        far = max(far, i + nums[i])
        if far >= len(nums) - 1:
            return True
    return False