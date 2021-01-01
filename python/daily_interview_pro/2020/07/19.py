"""
Remove Character to Create Palindrome

This problem was recently asked by Google:

Given a string, determine if you can remove any character to create a palindrome.

"""


def create_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return is_palindrome(s, i + 1, j) or is_palindrome(s, i, j - 1)
    return True


def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    print(create_palindrome("abcdcbea"))
    print(create_palindrome("abccba"))
    print(create_palindrome("abccaa"))
