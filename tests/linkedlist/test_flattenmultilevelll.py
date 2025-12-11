import unittest
from src.linkedlist.flattenmultilevelll import flatten_multi_level_list
from src.linkedlist.utils import from_multi_level_list_node_to_array, from_array_to_multi_level_list_node

class TestFlattenMultiLevelLinkedList(unittest.TestCase):

    def test_flatten_multi_level_linked_list(self):
        arg = from_array_to_multi_level_list_node([[1],[2,[[6],[7,[[10]]]]],[3],[4,[[8,[[11]]],[9]]],[5]])
        result = flatten_multi_level_list(arg)
        arrayResult = from_multi_level_list_node_to_array(result)
        self.assertEqual(arrayResult,
                         [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]] )