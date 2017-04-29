import unittest
from stack import Stack


class StackTestCase(unittest.TestCase):

    def setUp(self):
        self.testStack = Stack()
        self.testStack.push(4)
        self.testStack.push(6)

    def test_pop(self):
        self.assertEqual(self.testStack.pop(), 6)

    def test_push(self):
        self.assertEqual(self.testStack.push(2), [4, 6, 2])

    def test_peek(self):
        self.assertEqual(self.testStack.peek(), 6)

    def test_isEmpty(self):
        self.assertFalse(self.testStack.isEmpty())


if __name__ == '__main__':
    unittest.main()
