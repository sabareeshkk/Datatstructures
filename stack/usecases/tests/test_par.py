import unittest

from ..parChecker import parCheck


class ParCheckTest(unittest.TestCase):

    def setUp(self):
        self.parChecker = parCheck

    def test_balanced(self):
        return self.assertTrue(self.parChecker('{{([][])}()}'))

    def test_unbalanced(self):
        return self.assertFalse(self.parChecker('[{()]'))


if __name__ == '__main__':
    unittest.main()
