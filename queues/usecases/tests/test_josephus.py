import unittest

from ..josephus import josephusIdea


class josephusIdeaTest(unittest.TestCase):

    def setUp(self):
        self.personEscaped = josephusIdea(
            ["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)

    def test_escapedPerson(self):
        return self.assertEqual(self.personEscaped, "Susan")


if __name__ == '__main__':
    unittest.main()
