"""
infix expression to postfix converter
"""
from ..stack import Stack


def infixToPostFix(infixExp):
    operandList = []
    operatorStack = Stack()

    operatorPrecedence = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    for token in infixExp.split():

        if token.isalpha() or token.isdigit():
            operandList.append(token)
        elif token == '(':
            operatorStack.push(token)
        elif token == ')':
            while operatorStack.peek() != '(':
                topToken = operatorStack.pop()
                operandList.append(topToken)
            operatorStack.pop()

        else:
            while not operatorStack.isEmpty() and \
                    operatorPrecedence[operatorStack.peek()] >= operatorPrecedence[token]:

                operandList.append(operatorStack.pop())
            operatorStack.push(token)

    if not operatorStack.isEmpty():
        reverseOperatorStack = operatorStack.show()
        reverseOperatorStack.reverse()
        operandList.extend(reverseOperatorStack)

    return ' '.join(operandList)


if __name__ == "__main__":
    print infixToPostFix("A * B + C * D")
    print infixToPostFix("( A + B ) * ( C + D )")
