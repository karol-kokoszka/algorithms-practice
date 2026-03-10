import unittest
from src.graphs.prerequisites import prerequisites

class TestPrerequisites(unittest.TestCase):

    def test_prerequisites(self):
        self.assertEqual(prerequisites(3, [[0, 1], [1, 2], [2, 1]]), False)
        self.assertEqual(prerequisites(3, []), True)
        self.assertEqual(prerequisites(3, [[0, 1], [1, 2], [0, 2]]), True)
        self.assertEqual(prerequisites(5, [[0, 1], [1, 2], [0, 2], [3, 4]]), True)
        self.assertEqual(prerequisites(5, [[0, 1], [1, 2], [0, 2], [3, 4], [4, 3]]), False)