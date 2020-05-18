"""
Fix Brackets

This problem was recently asked by Twitter:

Given a string with only ( and ), find the minimum number of characters to add or subtract
to fix the string such that the brackets are balanced.

Example:
Input: '(()()'
Output: 1
Explanation:

The fixed string could either be ()() by deleting the first bracket, or (()()) by adding a bracket.
These are not the only ways of fixing the string,
there are many other ways by adding it in different positions!

"""

def solution(string):
    left_open = 0
    left_closed = 0

    for item in string:
        if item == "(":
            left_open += 1
        elif item == ")":
            if left_open == 0:
                left_closed += 1
            else:
                left_open -= 1

    return left_open + left_closed


if __name__ == "__main__":
    print(solution("(()("))