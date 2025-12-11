import unittest
from src.stacks.validparenthesisexpression import valid_parenthesis_expression

class TestValidParenthesisExpression(unittest.TestCase):

    def test_validparenthesisexpression(self):
        self.assertEqual(valid_parenthesis_expression('([]{})'), True)
        self.assertEqual(valid_parenthesis_expression(''), True)
        self.assertEqual(valid_parenthesis_expression('(([[]))'), False)
        self.assertEqual(valid_parenthesis_expression('((())'), False)
