import unittest
from src.graphs.connectthedots import connect_the_dots

class TestConnectTheDots(unittest.TestCase):

    def test_connect_the_dots(self):
        self.assertEqual(connect_the_dots([[1, 1], [2, 6], [3, 2], [4, 3], [7, 1]]), 15)
        self.assertEqual(connect_the_dots([]), 0)