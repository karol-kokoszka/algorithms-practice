import unittest
from src.dynamic.matrixpathways import matrix_pathways

class TestMatrixPathways(unittest.TestCase):

    def test_matrix_pathways(self):
        self.assertEqual(matrix_pathways(3, 3), 6)
        self.assertEqual(matrix_pathways(0, 0), 0)
        self.assertEqual(matrix_pathways(1, 1), 1)
        self.assertEqual(matrix_pathways(1, 2), 1)