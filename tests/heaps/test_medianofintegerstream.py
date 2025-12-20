import unittest
from src.heaps.medianofintegerstream import MedianOfAnIntegerStream

class TestMedianOfIntegerStream(unittest.TestCase):

    def test_median_of_integer_stream(self):
        # result = []
        # median = MedianOfAnIntegerStream()
        # median.add(3)
        # median.add(6)
        # result.append(median.get_median())
        # median.add(1)
        # result.append(median.get_median())
        # self.assertEqual(result, [4.5, 3.0])

        # result = []
        # median = MedianOfAnIntegerStream()
        # median.add(1)
        # result.append(median.get_median())
        # self.assertEqual(result, [1.0])

        result = []
        median = MedianOfAnIntegerStream()
        median.add(5)
        median.add(4)
        median.add(3)
        median.add(2)
        median.add(1)
        result.append(median.get_median())
        self.assertEqual(result, [3.0])
