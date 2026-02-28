import unittest
from src.graphs.matrixinfection import matrix_infection

class TestMatrixInfection(unittest.TestCase):

    def test_matrix_infection(self):
        self.assertEqual(matrix_infection([[1, 1, 1, 0],
                                           [0, 0, 2, 1], 
                                           [0, 1, 1, 0]]), 3)
        
        self.assertEqual(matrix_infection([[1, 1, 1, 1]]), -1)

        self.assertEqual(matrix_infection([[1, 1, 1, 2]]), 3)

        self.assertEqual(matrix_infection([[2,1,1,1],
                                           [1,2,1,1],
                                           [1,1,2,1],
                                           [1,1,1,2]]), 3)
        
        self.assertEqual(matrix_infection([[]]), 0)

        self.assertEqual(matrix_infection([[2,1,2,1],
                                           [1,1,1,1],
                                           [1,2,1,2],
                                           [2,1,1,2]]), 1)

        self.assertEqual(matrix_infection([[1,2,1],
                                           [0,0,0],
                                           [1,0,0]]), -1)