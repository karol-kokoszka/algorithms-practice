import unittest
from src.intervals.mergingoverlapingintervals import merge_overlapping_intervals
from src.intervals.utils import Interval

class TestMergingOverlapingIntervals(unittest.TestCase):

    def test_merging_overlaping_intervals(self):
        result = merge_overlapping_intervals(
            [Interval(3, 4), Interval(7, 8), Interval(2, 5), Interval(6, 7), Interval(1, 4)])
        for i in result:
            print(i.start, i.end)
        self.assertEqual(result,  [Interval(1, 5), Interval(6, 8)])                    
            