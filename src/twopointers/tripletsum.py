from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[List[int]]:
    out = []
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            out.append([left, right])
            oldLeft = left
            while left < right and nums[oldLeft] == nums[left]:
                left += 1
        elif nums[left] + nums[right] < target:
            oldLeft = left
            while left < right and nums[oldLeft] == nums[left]:
                left += 1
        else:
            oldRight = right
            while left < right and nums[oldRight] == nums[right]:
                right -= 1
    return out

def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    out = []

    n = 0
    while n < len(nums) - 2:
        sublist = nums[n + 1: len(nums)]
        responses = pair_sum_sorted(sublist, -(nums[n]))
        for res in responses:
            if len(res) > 0:
                out.append([nums[n], sublist[res[0]], sublist[res[1]]])
        curr = nums[n]
        while n < len(nums) and nums[n] == curr:
            n = n + 1
    return out
