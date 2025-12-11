import unittest
from src.heaps.utils import HeapImpl

class TestUtils(unittest.TestCase):

    def test_heap_insert(self):
        self.skipTest("")

        def compare(a: int, b: int) -> int:
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0

        heap = HeapImpl(compare)
        heap.insert(1) 
        heap.insert(6) 
        heap.insert(2) 
        heap.insert(8) 
        heap.insert(4) 
        heap.insert(2) 

        self.assertEqual(heap.data, [8, 6, 2, 1, 4, 2])

    def test_heap_build_heap(self):
        def compare(a: int, b: int) -> int:
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0

        heap = HeapImpl[int](compare, [1 ,6 ,2 ,8 ,4, 2])
        heap.build_heap()

        self.assertEqual(heap.data, [8, 6, 2, 1, 4, 2])

        heap = HeapImpl[int](compare, [1 ,1 ,1 ,1 ,1, 1])
        heap.build_heap()

        self.assertEqual(heap.data, [1 ,1 ,1 ,1 ,1, 1])

    def test_heap_extract_max(self):
        def compare(a: int, b: int) -> int:
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0

        heap = HeapImpl[int](compare, [1 ,6 ,2 ,8 ,4, 2], True)

        self.assertEqual(heap.extract_max(), 8)
        self.assertEqual(heap.extract_max(), 6)
        self.assertEqual(heap.extract_max(), 4)
