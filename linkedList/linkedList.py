"""
implement linked list in python
"""
from node import Node


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
        return self.head

    def size(self):
        current = self.head
        count = 0
        while current.next != None:
            current = current.getNext()
            count += 1

    def search(self, data):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, data):
        current = self.head
        previous = None
        removed = False

        while current != None and not removed:
            if current.getData() == data:
                if previous == None:
                    self.head = previous
                else:
                    previous.setNext(current.getNext())
                removed = True
            else:
                previous = current
                current = current.getNext()
        return removed


if __name__ == '__main__':
    unorderedList = UnorderedList()
    unorderedList.add(3)
    unorderedList.add(6)
    print unorderedList.search(3)
    print unorderedList.search(5)
    print unorderedList.remove(3)
    print unorderedList.remove(7)
