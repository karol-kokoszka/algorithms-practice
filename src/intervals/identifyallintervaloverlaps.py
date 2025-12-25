from src.intervals.utils import Interval
from typing import List

"""
Definition of Interval:
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

Start:
- start with index 0 of intervals1 and intervals2
- find the lowest of intervals1 and intervals2
- create support function that gets:
    - current interval
    - anchor to "other" list
    - actual position in "other" list
- function will return:
    - index of the last overlapping interval
    - list of overlapping intervals
- do it in loop unitl the "contra" list is empty
"""

def build_intervals(intervals1: List[Interval], intervals2: List[Interval], pos1: int, pos2: int):
    overlaps = []
    while pos2 < len(intervals2) and intervals2[pos2].start <= intervals1[pos1].end:
        overlaps.append(Interval(intervals2[pos2].start, min(intervals1[pos1].end, intervals2[pos2].end)))
        pos2 += 1
    return pos2 if pos2 == 0 or intervals2[pos2 - 1].end <= intervals1[pos1].end else pos2 - 1, overlaps

def identify_all_interval_overlaps(intervals1: List[Interval], intervals2: List[Interval]) -> List[Interval]:
    i, j = 0, 0
    overlaps = []

    while i < len(intervals1) and j < len(intervals2):
        if intervals1[i].start < intervals2[j].start:
            j, result = build_intervals(intervals1, intervals2, i, j)
            overlaps += result
            i += 1
        else:
            i, result = build_intervals(intervals2, intervals1, j, i)
            overlaps += result
            j += 1

    return overlaps