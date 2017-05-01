import unittest

from ..queue import Queue


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)

    def test_enqueue(self):
        return self.assertEqual(self.queue.show(), [1, 2])

    def test_dequeue(self):
        return self.assertEqual(self.queue.dequeue(), 1)

    def test_isEmpty(self):
        return self.assertFalse(self.queue.isEmpty())


if __name__ == '__main__':
    unittest.main()
