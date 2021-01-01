"""
Word Concatenation

This problem was recently asked by LinkedIn:

Given a set of words, find all words that are concatenations of other words in the set.

"""


def solution(words):
    wordDict = set(words)
    cache = {}
    return [word for word in words if can_form(word, wordDict, cache)]


def can_form(word, wordDict, cache):
    if word in cache:
        return cache[word]
    for index in range(1, len(word)):
        prefix = word[:index]
        suffix = word[index:]
        if prefix in wordDict:
            if suffix in wordDict or can_form(suffix, wordDict, cache):
                cache[word] = True
                return True
    cache[word] = False
    return False


if __name__ == "__main__":
    words = ['rat', 'cat', 'cats', 'dog', 'catsdog', 'dogcat', 'dogcatrat']
    print(solution(words))
    # ['catsdog', 'dogcat', 'dogcatrat']