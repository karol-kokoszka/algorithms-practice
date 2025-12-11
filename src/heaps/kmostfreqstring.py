from typing import List
from collections import defaultdict
from src.heaps.utils import HeapImpl

"""
Find the k most frequently occurring strings in an array, 
and return them sorted by frequency in descending order. 
If two strings have the same frequency, sort them in lexicographical order.
"""
def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    occurrences = defaultdict(int)
    for word in strs:
        occurrences[word] += 1
    
    def compare(a: tuple, b: tuple) -> int:
        if a[1] > b[1]:
            return 1
        if a[1] < b[1]:
            return -1
        if a[0] > b[0]:
            return -1
        if a[0] < b[0]:
            return 1
        return 0
    
    heap = HeapImpl[tuple](compare=compare, data=list(occurrences.items()), build=True)
    result = []
    for i in range(min(k, len(occurrences.keys()))):
        result.append(heap.extract_max()[0])
    return result
    
