"""
Validate Balanced Parentheses

This problem was recently asked by Uber:

Imagine you are building a compiler.
Before running any code, the compiler must check that the parentheses in the program are balanced.
Every opening bracket must have a corresponding closing bracket.

We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False

"""

def solution(string):
    open_parens = "({["
    closing_parens = ")}]"
    stack = []

    for char in string:
        if char in open_parens:
            stack.append(char)
        elif char in closing_parens:
            if not stack:
                return False

            if open_parens.index(stack.pop()) != closing_parens.index(char):
                return False

    return len(stack) == 0


if __name__ == "__main__":
    # Test Program
    s = "()(){(())"
    # should return False
    print(solution(s))

    s = ""
    # should return True
    print(solution(s))

    s = "([{}])()"
    # should return True
    print(solution(s))
