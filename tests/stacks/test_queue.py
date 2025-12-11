import unittest
from src.stacks.queue import Queue

class TestQueue(unittest.TestCase):

    def test_queue(self):
        output = []

        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        output.append(q.dequeue())
        q.enqueue(3)
        output.append(q.peek())

        print(output)