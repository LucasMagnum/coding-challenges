"""
Remove Character to Create Palindrome

This problem was recently asked by Google:

Given a string, determine if you can remove any character to create a palindrome.

"""

def create_palindrome(string):
    left, right = 0, len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return is_palindrome(string, left + 1, right) or is_palindrome(string, left, right - 1)
    return True


def is_palindrome(string, left, right):
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(create_palindrome("abcdcbea"))
    # True
    print(create_palindrome("abccba"))
    # True
    print(create_palindrome("abccaa"))
    # False