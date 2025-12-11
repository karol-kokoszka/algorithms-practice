from typing import List
from collections import Counter, defaultdict

def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    occurencesOfOnRight = Counter(nums)
    occurencesOfOnLeft = defaultdict(int)
    total = 0
    for n in nums:
        occurencesOfOnRight[n] -= 1
        if n % r == 0:
            prev = n // r
            next = n * r
            total += occurencesOfOnLeft[prev] * occurencesOfOnRight[next]
        occurencesOfOnLeft[n] += 1
    return total