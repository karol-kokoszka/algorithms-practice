from typing import List
from collections import defaultdict

def k_sum_subarrays(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return 0
    
    sums = []    
    current = 0
    occurrences = defaultdict(int)
    occurrences[0] += 1

    sums.append(nums[0])
    current += occurrences[sums[0] - k]
    occurrences[nums[0]] += 1

    for i in range(1, len(nums)):
        sums.append(sums[i-1] + nums[i])
        current += occurrences[sums[-1] - k]
        occurrences[sums[i-1] + nums[i]] += 1

    return current
