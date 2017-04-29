"""
checks wether an expresion is valid or not
"""
from ..stack import Stack


def parCheck(expression):

    newStack = Stack()
    closeParams = {'}': '{', ')': '(', ']': '['}

    for element in expression:

        if element in "([{":
            newStack.push(element)
        else:
            if closeParams[element] == newStack.peek():
                newStack.pop()

    return newStack.size() == 0


if __name__ == "__main__":
    parCheck('{{([][])}()}')
