"""
Reverse Polish Notation Calculator

This problem was recently asked by Facebook:

Given an expression (as a list) in reverse polish notation, evaluate the expression.
Reverse polish notation is where the numbers come before the operand.
Note that there can be the 4 operands '+', '-', '*', '/'.

You can also assume the expression will be well formed.

Example
Input: [1, 2, 3, '+', 2, '*', '-']
Output: -9
The equivalent expression of the above reverse polish notation would be
 (1 - ((2 + 3) * 2)).

"""

def solution(items):
    stack = []
    operands = {
        "+": lambda a,b: a + b,
        "-": lambda a,b: a - b,
        "*": lambda a,b: a * b,
        "/": lambda a,b: a / b,
    }

    for item in items:
        if item in operands:
            a, b = stack.pop(), stack.pop()
            stack.append(operands[item](b, a))
        else:
            stack.append(item)

    return stack[0]

if __name__ == "__main__":
    print(solution([1, 2, 3, "+", 2, "*", "-"]))