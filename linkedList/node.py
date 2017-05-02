"""
Implement LinkedList Nodes.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, next):
        self.next = next


if __name__ == '__main__':
    node = Node(2)
    print node.getData()
