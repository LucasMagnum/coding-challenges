"""
Spreadsheet Column Title

This problem was recently asked by Amazon:

MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA,
BB, ..., ZZ, AAA, AAB, ... etc. In other words, column 1 is named "A", column 2 is "B",
column 26 is "Z", column 27 is "AA" and so forth.

Given a positive integer, find its corresponding column name.

Examples:
Input: 26
Output: Z

Input: 51
Output: AY

Input: 52
Output: AZ

Input: 676
Output: YZ

Input: 702
Output: ZZ

Input: 704
Output: AAB

"""
import string

letters = list(string.ascii_uppercase)


def solution(number):
    if number <= len(letters):
        return letters[number - 1]

    return solution((number - 1) // len(letters)) + solution(number % len(letters))


if __name__ == "__main__":
    assert solution(1) == "A"
    assert solution(28) == "AB"
    assert solution(456976) == "YYYZ"