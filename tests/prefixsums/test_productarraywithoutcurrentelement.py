import unittest
from src.prefixsums.productarraywithoutcurrentelement import product_array_without_current_element

class TestProductArrayWithoutCurrentElement(unittest.TestCase):

    def test_product_array_without_current_element(self):
        self.assertEqual(product_array_without_current_element([2, 3, 1, 4, 5]), [60, 40, 120, 30, 24])