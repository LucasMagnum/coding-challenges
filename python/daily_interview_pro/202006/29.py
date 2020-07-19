"""
Anagrams in a string

This problem was recently asked by Twitter:

Given 2 strings s and t, find and return all indexes in string s where t is an anagram.
"""

from collections import defaultdict


def find_anagrams(string, part):
    result = []

    char_map = defaultdict(int)
    for char in part:
        char_map[char] += 1

    part_size = len(part)

    for idx, char in enumerate(string):
        if idx >= part_size:
            old_char = string[idx - part_size]
            char_map[old_char] += 1
            if char_map[old_char] == 0:
                del char_map[old_char]

        char_map[char] -= 1
        if char_map[char] == 0:
            del char_map[char]

        if idx + 1 >= part_size and len(char_map) == 0:
            result.append(idx - part_size + 1)

    return result


if __name__ == "__main__":
    print(find_anagrams("acdbacdacba", "abc"))
    # [3, 7]
