"""
Convert Roman Numerals to Decimal

This problem was recently asked by Twitter:

Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.

Example:
Input: IX
Output: 9

Input: VII
Output: 7

Input: MCMIV
Output: 1904

"""

values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def solution(string):
    prev = 0
    total = 0

    for i in string[::-1]:
        current = values[i]
        if prev > current:
            total -= current
        else:
            total += current
        prev = current

    return total


if __name__ == "__main__":
    print(solution("MCMX"))
