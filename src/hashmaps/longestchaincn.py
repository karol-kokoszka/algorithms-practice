from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    numberExists = {}
    max = 0
    for n in nums:
        numberExists[n] = None
    for n in nums:
        if numberExists.get(n-1, "N/A") == None:
            continue
        i = 0
        curr = n
        while numberExists.get(curr + i, "N/A") == None:
            i = i + 1
        if i > max:
            max = i
    return max