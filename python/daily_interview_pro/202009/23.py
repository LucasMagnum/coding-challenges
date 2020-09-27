"""
Reverse Polish Notation Calculator

This problem was recently asked by Facebook:

Given an expression (as a list) in reverse polish notation,
evaluate the expression.
Reverse polish notation is where the numbers come before the operand.
Note that there can be the 4 operands '+', '-', '*', '/'.
You can also assume the expression will be well formed.

Example
Input: [1, 2, 3, '+', 2, '*', '-']
Output: -9
The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).

"""


def reverse_polish_notation(expression):
    stack = []
    operands = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    for current in expression:
        if current in operands:
            right, left = stack.pop(), stack.pop()
            current = operands[current](left, right)
        stack.append(current)

    return stack[0]



if __name__ == "__main__":
    # 1 - (2 + 3) * 2
    print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
    # -9