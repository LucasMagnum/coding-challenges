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

def solution(string_a, string_b):
    if len(string_a) != len(string_b):
        return False

    if string_a == string_b and len(string_a) > len(set(string_a)):
        return True

    diff_a = []
    diff_b = []

    for i in range(len(string_a)):
        if len(diff_a) > 2:
            return False

        if string_a[i] != string_b[i]:
            diff_a += string_a[i]
            diff_b += string_b[i]

    if len(diff_a) != 2:
        return False

    if diff_a[0] == diff_b[1] and diff_a[1] == diff_b[0]:
        return True

    return False


if __name__ == "__main__":
    print(solution('aaaaaaabc', 'aaaaaaacb'))
    # True
    print(solution('aaaaaabbc', 'aaaaaaacb'))
    # False