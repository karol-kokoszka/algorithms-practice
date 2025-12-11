from typing import List

def largest_container(heights: List[int]) -> int:
    left, right, maxContainer = 0, len(heights) - 1, 0
    while left < right:
        maxContainer = max(maxContainer, min(heights[left], heights[right]) * (right - left))
        if heights[left] < heights[right]:
            left+=1
        else:
            right-=1
    return maxContainer