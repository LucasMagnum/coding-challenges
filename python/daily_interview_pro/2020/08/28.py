"""
Ransom Note

This problem was recently asked by Google:

A criminal is constructing a ransom note. In order to disguise his handwriting, he is cutting out letters from a magazine.

Given a magazine of letters and the note he wants to write, determine whether he can construct the word.

"""
from collections import defaultdict


def solution(magazine, note):
    letters = defaultdict(int)

    for c in magazine:
        letters[c] += 1

    for c in note:
        if letters[c] <= 0:
            return False
        letters[c] -= 1

    return True


if __name__ == "__main__":
    print(solution(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
    # True

    print(solution(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
    # False