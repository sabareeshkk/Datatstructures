"""
Implementing Queue using List
"""


class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            raise IndexError('Cannot Dequeue Empty.Its Empty:(')

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def show(self):
        return self.queue


if __name__ == '__main__':
    queue = Queue()
