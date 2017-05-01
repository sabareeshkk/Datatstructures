"""
Convert decimal number to binary octal and hex
"""
from ..stack import Stack

DIGITS = "0123456789ABCDEF"


def decToOther(decNumber, base, stack=None):

    if decNumber <= 0:
        stack = checkStack(stack)
        return stack
    else:
        stack = checkStack(stack)
        rem = decNumber % base
        stack.push(str(DIGITS[rem]))
        decNumber = decNumber // base
        return decToOther(decNumber, base, stack)


def checkStack(stack):
    if stack is None:
        stack = Stack()
    return stack


if __name__ == "__main__":
    binary = decToOther(233, 2).show()
    binary.reverse()
    print ''.join(binary)
