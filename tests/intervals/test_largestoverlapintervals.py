import unittest
from src.intervals.largestoverlapintervals import largest_overlap_of_intervals
from src.intervals.utils import Interval

class TestLargestOverlapIntervals(unittest.TestCase):

    def test_largest_overlap_intervals(self):
        intervals = [Interval(1, 3), Interval(5, 7), Interval(2, 6), Interval(4, 8)]
        self.assertEqual(largest_overlap_of_intervals(intervals), 3)