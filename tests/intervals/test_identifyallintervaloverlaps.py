import unittest
from src.intervals.utils import Interval
from src.intervals.identifyallintervaloverlaps import identify_all_interval_overlaps, build_intervals

class TestIdentifyAllIntervalOverlaps(unittest.TestCase):

    def test_identify_all_interval_overlaps(self):
        interval1 = [Interval(1, 4), Interval(5, 6), Interval(9, 10)]
        interval2 = [Interval(2, 7), Interval(8, 9)]
        result = identify_all_interval_overlaps(interval1, interval2)

        expected = [Interval(2, 4), Interval(5, 6), Interval(9, 9)]

        self.assertEqual(result, expected)

        interval1 = [Interval(1, 2), Interval(3, 4), Interval(5, 6)]
        interval2 = [Interval(7, 8), Interval(9, 10)]
        result = identify_all_interval_overlaps(interval1, interval2)

        expected = []

        self.assertEqual(result, expected)


    def test_build_intervals(self):
        self.skipTest("")

        interval1 = [Interval(1, 8), Interval(9, 10)]
        interval2 = [Interval(4, 6), Interval(7, 7), Interval(8, 10)]

        pos2, overlaps = build_intervals(interval1, interval2, 0, 0)

        self.assertEqual(overlaps, [Interval(4, 6), Interval(7, 7), Interval(8, 8)])
        self.assertEqual(pos2, 2)

        interval1 = [Interval(1, 8), Interval(9, 10)]
        interval2 = [Interval(4, 6), Interval(7, 7), Interval(8, 8)]

        pos2, overlaps = build_intervals(interval1, interval2, 0, 0)

        self.assertEqual(overlaps, [Interval(4, 6), Interval(7, 7), Interval(8, 8)])
        self.assertEqual(pos2, 3)
