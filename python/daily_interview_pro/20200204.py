"""
Longest Palindromic Substring

This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards.

Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""


def solution(string: str) -> str:
    if not string:
        return string

    max_length = 0
    start_palindrome = 0

    def expand_from_center(start, end):
        nonlocal max_length, start_palindrome

        while start >= 0 and end < len(string) and string[start] == string[end]:
            start -= 1
            end += 1

        length = end - start - 1

        if length > max_length:
            max_length = length
            start_palindrome = start + 1

    for index in range(len(string)):
        # Check of odd length palindromes
        expand_from_center(index, index)

        # Check for even length palindromes
        expand_from_center(index, index + 1)

    return string[start_palindrome : start_palindrome + max_length]


if __name__ == "__main__":
    string = "abscatelucassaculgeleadeira"
    print(f"Solution({string}) -> ", solution(string))
