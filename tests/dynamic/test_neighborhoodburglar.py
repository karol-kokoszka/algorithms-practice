import unittest
from src.dynamic.nieghborhoodburglar import neighborhood_burglary

class TestNeighborhoodBurglar(unittest.TestCase):

    def test_neighborhood_burglar(self):
        self.assertEqual(neighborhood_burglary([200, 300, 200, 50]), 400)
        self.assertEqual(neighborhood_burglary([]), 0)
        self.assertEqual(neighborhood_burglary([200]), 200)
        self.assertEqual(neighborhood_burglary([200, 300]), 300)
        self.assertEqual(neighborhood_burglary([200, 10, 10, 300, 10]), 500)