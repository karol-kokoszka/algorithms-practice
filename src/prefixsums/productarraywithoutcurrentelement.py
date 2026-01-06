from typing import List

def product_array_without_current_element(nums: List[int]) -> List[int]:
    left, right = [1] * len(nums), [1] * len(nums)

    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]
        right[len(nums) - 1 - i] = right[len(nums) - i] * nums[len(nums) - i]
    
    result = []
    for i in range(len(nums)):
        result.append(left[i] * right[i])

    return result