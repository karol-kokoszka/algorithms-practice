import unittest
from src.stacks.maximumofsllidingwindows import maximums_of_sliding_window

class TestMaximumsOfSlidingWindows(unittest.TestCase):

    def test_maximums_of_sliding_windows(self):
        self.assertEqual(maximums_of_sliding_window([3, 2, 4, 1, 2, 1, 1], k = 4), [4, 4, 4, 2])
        self.assertEqual(maximums_of_sliding_window([3, 2, 4], k = 4), [])
        self.assertEqual(maximums_of_sliding_window([], k = 4), [])
