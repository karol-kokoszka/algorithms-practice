import unittest
from src.greedy.gasstations import gas_stations

class TestGasStations(unittest.TestCase):\

    def test_gas_stations(self):
        self.assertEqual(gas_stations(gas = [2, 5, 1, 3], cost = [3, 2, 1, 4]), 1)  
        self.assertEqual(gas_stations(gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]), 3)  
        self.assertEqual(gas_stations(gas = [2, 3, 4], cost = [3, 4, 3]), -1)  
