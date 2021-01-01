"""
Buddy Strings

This problem was recently asked by AirBNB:
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
    Input: A = "ab", B = "ba"
    Output: true

Example 2:
    Input: A = "ab", B = "ab"
    Output: false

Example 3:
    Input: A = "aa", B = "aa"
    Output: true

Example 4:
    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true

Example 5:
    Input: A = "", B = "aa"
    Output: false
"""


def solution(first: str, second: str):
    if len(first) != len(second):
        return False

    # If they are the same with duplicated caracters
    if first == second and len(first) != len(set(first)):
        return True

    diff = 0
    for i, j in zip(range(len(first)), range(len(second))):
        if first[i] != second[j]:
            diff += 1

    return diff == 2


if __name__ == "__main__":
    assert solution("ab", "ba")
    assert solution("aa", "aa")
    assert solution("aaaaaaabc", "aaaaaaacb")
    assert solution("aaaaaabbc", "aaaaaaacb") is False
    assert solution("", "aa") is False
