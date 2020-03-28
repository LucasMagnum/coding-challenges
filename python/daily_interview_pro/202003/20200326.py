"""
Minimum Removals for Valid

This problem was recently asked by Uber:

You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("

"""

def solution(string):
    opened = 0
    invalid = 0

    for c in string:
        if c == "(":
            opened += 1
        elif c == ")":
            if opened > 0:
                opened -= 1
            else:
                invalid += 1
    
    invalid += opened
    return invalid


if __name__ == "__main__":
    value = "()())(()"
    print(solution(value))