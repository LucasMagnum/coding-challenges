"""
Top K Frequent words

This problem was recently asked by AirBNB:

Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will contain only lower-case letters.

Example:
Input: ["daily", "interview", "pro", "pro",
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]

"""

from collections import Counter, defaultdict


def solution(words, k):
    counter = Counter(words)
    freqs = defaultdict(list)

    for word, count in counter.items():
        freqs[count].append(word)

    res = []
    for i in range(len(words), 0, -1):
        if i in freqs:
            for word in freqs[i]:
                res.append((word, i))

        if len(res) >= k:
            break

    res = sorted(res, reverse=True, key=lambda x: x[1])
    return [element[0] for element in res]


if __name__ == "__main__":
    words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
    k = 2
    print(solution(words, k))
    # ['pro', 'daily']