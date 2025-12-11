import unittest
from src.binarysearch.matrixsearch import matrix_search

class TestMatrixSearch(unittest.TestCase):

    def test_matrix_search(self):
        self.assertEqual(matrix_search([[2,3,4,6],[7,10,11,17],[20,21,24,33]], 21), True)
        self.assertEqual(matrix_search([[2,3,4,6],[7,10,11,17],[20,21,24,33]], 0), False)
        self.assertEqual(matrix_search([[2,3,4,6],[7,10,11,17],[20,21,24,33]], 12), False)