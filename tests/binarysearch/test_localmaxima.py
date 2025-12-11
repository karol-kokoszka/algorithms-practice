import unittest
from src.binarysearch.localmaxima import local_maxima_in_array

class TestLocalMaxima(unittest.TestCase):

    def test_local_maxima_in_array(self):
        self.assertEqual(local_maxima_in_array([1, 4, 3, 2, 3]), 1)
