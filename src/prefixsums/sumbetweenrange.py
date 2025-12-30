from typing import List

class SumBetweenRange:

    def __init__(self, nums: List[int]):
        self.sums = []
        if len(nums) > 0:
            self.sums.append(nums[0])
        for i in range(1, len(nums)):
            self.sums.append(self.sums[i - 1] + nums[i])

    def sum_range(self, i: int, j: int):
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]