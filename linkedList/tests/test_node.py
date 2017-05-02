import unittest

from ..node import Node


class NodeTest(unittest.TestCase):

    def setUp(self):
        self.node = Node(4)
        self.node.setNext(None)

    def test_intialData(self):
        return self.assertEqual(self.node.getData(), 4)

    def test_getData(self):
        self.node.setData(3)
        return self.assertEqual(self.node.getData(), 3)

    def test_next(self):
        return self.assertEqual(self.node.getNext(), None)


if __name__ == '__main__':
    unittest.main()
