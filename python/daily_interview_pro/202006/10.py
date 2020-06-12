"""
First recurring character

This problem was recently asked by Amazon:

Given a string, return the first recurring letter that appears.
If there are no recurring letters, return None.

Example:
Input: qwertty
Output: t

Input: qwerty
Output: None

"""


def solution(string):
    checker = 0
    for char in string:
        if (checker & (1 << ord(char))):
            return char
        checker ^= 1 << ord(char)
    return None


if __name__ == "__main__":
    print(solution("qwerty"))
    print(solution("qwerty"))