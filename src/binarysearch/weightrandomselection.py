from typing import List, Tuple
import random

class WeightedRandomSelection:

    def __init__(self, weights: List[int]):
        self.range = len(weights) - 1
        self.total = 0
        self.buckets = []
        currentLowerBound = 0
        for i in range(len(weights)):
            self.total += weights[i]
            self.buckets.append((currentLowerBound, currentLowerBound + weights[i] - 1))
            currentLowerBound = currentLowerBound + weights[i]

    def select(self) -> int:
        val = random.randint(0, self.total - 1)
        left, right = 0, self.range
        
        while left < right:
            mid = left + (right - left) // 2
            if self.buckets[mid][1] < val:
                left = mid + 1
            else:
                right = mid
        return left
    