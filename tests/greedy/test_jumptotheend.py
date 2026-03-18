import unittest
from src.greedy.jumptotheend import jump_to_the_end

class TestJumpToTheEnd(unittest.TestCase):

    def test_jump_to_the_end(self):
        # self.assertEqual(jump_to_the_end([3, 2, 0, 2, 5]), True)
        self.assertEqual(jump_to_the_end([2,1,0,3]), False)