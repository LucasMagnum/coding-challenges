"""
Group Words that are Anagrams

This problem was recently asked by AirBNB:

Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

"""
from collections import defaultdict


def solution(words):
    groups = defaultdict(list)

    for word in words:
        groups["".join(sorted(word))].append(word)
    
    return list(groups.values())


if __name__ == "__main__":
    print(solution(['abc', 'bcd', 'cba', 'cbd', 'efg']))