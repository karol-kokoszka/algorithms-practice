import unittest
from src.backtracking.nqueens import n_queens

class TestNQueens(unittest.TestCase):

    def test_n_queens(self):
        self.assertEqual(n_queens(4), 2)
        self.assertEqual(n_queens(0), 1)        