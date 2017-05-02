import unittest

from ..linkedList import UnorderedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.linkedList = UnorderedList()

    def test_add(self):
        newItem = self.linkedList.add(3)
        return self.assertEqual(newItem.getData(), 3)

    def test_search(self):
        self.linkedList.add(3)
        found = self.linkedList.search(3)
        return self.assertTrue(found)

    def test_remove(self):
        self.linkedList.add(3)
        removed = self.linkedList.remove(3)
        return self.assertTrue(removed)
