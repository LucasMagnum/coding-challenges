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


def first_recurring_char(string):
    checker = 0

    for char in string:
        mask = 1 << (ord(char) - ord("a"))
        if checker & mask:
            return char
        checker |= mask

    return


if __name__ == "__main__":
    print(first_recurring_char('qwertty'))
    # t

    print(first_recurring_char('qwerty'))
    # None