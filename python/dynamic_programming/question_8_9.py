"""
    Parens:
        Implement an algorithm to print all valid (properly opened and closed) combinations o
        n pairs of parentheses.
"""
import sys


def brute_force(n):
    parens = set()
    
    if n == 0:
        parens.add("")
    else:
        previous = brute_force(n - 1)
        for string in previous:
            for index in range(len(string)):
                if string[index] == "(" or string[index] == ")":
                    parens.add(string[:index + 1] + "()" + string[index + 1:])
        parens.add("()" + string)
    
    return parens


def recursive(n):
    solutions = []
    string = " " * n * 2

    def _build_string(left_remaining, right_remaining, string, index):
        if left_remaining < 0 or right_remaining < left_remaining: 
            return
        
        if left_remaining == 0 and right_remaining == 0:
            solutions.append("".join(string))
        else:
            string[index] = "("
            _build_string(left_remaining - 1, right_remaining, string, index + 1)

            string[index] = ")"
            _build_string(left_remaining, right_remaining - 1, string, index + 1)

    _build_string(n * 2, n * 2, list(string), 0)
    return solutions


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = 1

    print("Solution: ", brute_force(n))
    print("Solution: ", recursive(n))