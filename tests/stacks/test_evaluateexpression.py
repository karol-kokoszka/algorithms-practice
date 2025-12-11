import unittest
from src.stacks.evaluateexpression import evaluate_expression, transform_to_rpn

class TestEvaluateExpression(unittest.TestCase):

    def test_transform_to_rpn(self):
        self.assertEqual(transform_to_rpn('18-(7+(2-4))'), ['18', '7', '2', '4', '-', '+', '-'])

    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression('18-(7+(2-4))'), 13)
        self.assertEqual(evaluate_expression('-5+10'), 5)
        self.assertEqual(evaluate_expression('4+(-5+10)'), 9)
        self.assertEqual(evaluate_expression(''), 0)