from typing import List

"""
Given an integer array and a target value, find all unique combinations in the array where the numbers 
in each combination sum to the target. Each number in the array may be used an unlimited number of times in the combination.
"""
def combinations_of_sum_k(nums: List[int], target: int) -> List[List[int]]:
    res = []

    def backtracking(current: List[int], index, currentSum: int) -> None:
        if currentSum > target:
            return 
        if currentSum == target:
            res.append(current[:])
            return 
        for i in range(index, len(nums)):
            current.append(nums[i])
            currentSum += nums[i]
            backtracking(current, i, currentSum)
            current.pop()
            currentSum -= nums[i]

    backtracking([], 0, 0)    
    return res
