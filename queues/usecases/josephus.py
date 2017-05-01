"""
Implementing josephus problem
https://en.wikipedia.org/wiki/Josephus_problem
"""
from ..queue import Queue


def josephusIdea(personsList, limit):

    personQueue = Queue()

    for person in personsList:
        personQueue.enqueue(person)

    while personQueue.size() != 1:

        for count in range(limit):
            personQueue.enqueue(personQueue.dequeue())

        personQueue.dequeue()
    return personQueue.dequeue()


if __name__ == '__main__':
    print josephusIdea(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
