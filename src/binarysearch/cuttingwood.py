from typing import List

"""
You are given an array representing the heights of trees, and an integer k representing 
the total length of wood that needs to be cut.

For this task, a woodcutting machine is set to a certain height, H .
The machine cuts off the top part of all trees taller than H, 
while trees shorter than H remain untouched. Determine the highest possible 
setting of the woodcutter (H) so that it cuts at least k meters of wood.

Assume the woodcutter cannot be set higher than the height of the tallest tree in the array.
"""
def cutting_wood(heights: List[int], k: int) -> int:
    if k == 0:
        return tallestTree(heights)
    left, right = 0, tallestTree(heights)
    while left < right:
        mid = left + (right - left) // 2 
        if gainedWood(heights, mid) >= k:
            left = mid + 1
        else:
            right = mid
    return left - 1

def tallestTree(heights: List[int]) -> int:
    tallest = 0
    for h in heights:
        if h > tallest:
            tallest = h
    return tallest

def gainedWood(heights: List[int], cutHeight: int) -> int:
    gained = 0
    for h in heights:
        if h > cutHeight:
            gained += h - cutHeight
    return gained
