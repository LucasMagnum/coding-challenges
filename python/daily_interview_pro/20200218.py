"""
Create a Simple Calculator

This problem was recently asked by Google:

Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properly formed.


Example:
    Input: - ( 3 + ( 2 - 1 ) )
    Output: -4

"""


def solution(expression, index=0):
    result = 0
    op = "+"

    while index < len(expression):
        char = expression[index]

        if char.isdigit():
            if op == "+":
                result += int(char)
            else:
                result -= int(char)
        elif char in ("+", "-"):
            op = char

        elif char == "(":
            n, index = solution(expression, index + 1)
            if op == "+":
                result += n
            else:
                result -= n
        elif char == ")":
            return result, index

        index += 1

    return (result, index)


if __name__ == "__main__":
    expression = "2 - (3 + ( 2 - 1 ) ) + 4 - 2"
    print(f"Solution({expression}) ->", solution(expression))
