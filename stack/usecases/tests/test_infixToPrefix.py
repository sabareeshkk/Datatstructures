import unittest

from ..infixToPostfix import infixToPostFix


class InfixToPostFixTest(unittest.TestCase):

    def setUp(self):
        self.postfix = infixToPostFix

    def test_withParanthesis(self):
        return self.assertEqual(self.postfix(
            "( A + B ) * ( C + D )"), 'A B + C D + *')

    def test_simple(self):
        return self.assertEqual(self.postfix("A + B * C"), 'A B C * +')


if __name__ == '__main__':
    unittest.main()
