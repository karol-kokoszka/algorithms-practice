from typing import List
from src.intervals.utils import Interval

def merge_overlapping_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x.start)
    merged_intervals = []

    currentStartPos = 0
    currentMaxEnd = intervals[0].end
    j = 1
    while j < len(intervals):
        if intervals[j].start > currentMaxEnd:
            merged_intervals.append(Interval(intervals[currentStartPos].start, currentMaxEnd))
            currentStartPos = j
        currentMaxEnd = max(intervals[j].end, currentMaxEnd)
        j += 1
    merged_intervals.append(Interval(intervals[currentStartPos].start, currentMaxEnd))
    return merged_intervals
