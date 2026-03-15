from typing import List

def find_all_subsets(nums: List[int]) -> List[List[int]]:
    res = []
    backtracking(0, [], nums, res)    
    return res

def backtracking(i: int, curr: List[int], nums: List[int], res: List[List[int]]) -> None:
    if i == len(nums):
        res.append(curr[:])
        return
    
    curr.append(nums[i])
    backtracking(i + 1, curr, nums, res)
    curr.pop()
    backtracking(i + 1, curr, nums, res)
