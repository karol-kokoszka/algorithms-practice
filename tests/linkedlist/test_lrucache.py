import unittest
from src.linkedlist.lrucache import LRUCache

class TestLRUCache(unittest.TestCase):

    def test_lru_cache(self):
        result = []

        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        result.append(cache.get(1))
        cache.put(3, 3)
        result.append(cache.get(2))
        cache.put(4, 4)
        result.append(cache.get(1))
        result.append(cache.get(3))
        result.append(cache.get(4))

        self.assertEqual(result, [1,-1,-1,3,4])