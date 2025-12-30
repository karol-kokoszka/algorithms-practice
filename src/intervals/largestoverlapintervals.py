from typing import List
from src.intervals.utils import Interval

def largest_overlap_of_intervals(intervals: List[Interval]) -> int:
    events = []
    
    for i in intervals:
        events.append((i.start, 1))
        events.append((i.end, -1))
    
    events.sort()
    maximum = 0
    current = 0
    for e in events:
        current += e[1]
        maximum = max(maximum, current)

    return maximum