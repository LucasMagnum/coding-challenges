"""
Character Map

This problem was recently asked by Google:

Given two strings, find if there is a one-to-one mapping of
characters between the two strings.

Example
Input: abc, def
Output: True # a -> d, b -> e, c -> f

Input: aab, def
Ouput: False # a can't map to d and e
"""


def has_character_map(str1, str2):
    if len(str1) != len(str2):
        return False

    char_map = {}

    for char1, char2 in zip(str1, str2):
        if char1 not in char_map:
            char_map[char1] = char2

        if char_map[char1] != char2:
            return False

    return True


if __name__ == "__main__":
    print(has_character_map("abc", "def"))
    # True
    print(has_character_map("aac", "def"))
    # False
