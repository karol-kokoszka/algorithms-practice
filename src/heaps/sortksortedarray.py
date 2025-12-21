from typing import List
import heapq

def sort_a_k_sorted_array(nums: List[int], k: int) -> List[int]:
    currentHeap = nums[:2*k + 1 if 2*k + 1 < len(nums) else len(nums)]
    heapq.heapify(currentHeap)

    i = 0
    while i < len(nums) - len(currentHeap):
        nums[i] = heapq.heappop(currentHeap)
        heapq.heappush(currentHeap, nums[i + len(currentHeap) + 1])
        i += 1
    j = 0
    while currentHeap:
        nums[i + j] = heapq.heappop(currentHeap)
        j += 1

    return nums