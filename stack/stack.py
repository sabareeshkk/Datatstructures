"""
Implementing Stack Datastructure in Python
Using List 
"""


class Stack(object):
    """
    Creates a stack using list
    """
    def __init__(self):
        """
        Initializing stack array
        param: None
        return: None
        """
        self.stack = []

    def push(self, value):
        """
        push value into the list
        """
        self.stack.append(value)
        return self.stack

    def pop(self):
        """
        Remove newly inserted value from list
        """
        return self.stack.pop()

    def isEmpty(self):
        """
        check list is empty or not
        """
        return len(self.stack) <= 0

    def peek(self):
        """
        returns the newly inserted element
        """
        return self.stack[-1]

    def size(self):
        """
        size of the list
        """
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
