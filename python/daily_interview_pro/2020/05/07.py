"""
Top K Frequent words

This problem was recently asked by AirBNB:

Given a non-empty list of words, return the k most frequent words. 
The output should be sorted from highest to lowest frequency,
and if two words have the same frequency, the word with lower alphabetical order comes first.
Input will contain only lower-case letters.

Example:
Input: ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]

"""
from collections import defaultdict


def solution(words, k):
    """
    We can count the frequency of words and group them by this frequency. 
    To do so, we iterate through the input, pairing each word to its frequency. 
    Next, we group them by frequency, combining words that occur once, twice, and so on.
    Finally, we sort the final list.
    """

    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    freqs = defaultdict(list)
    for word, count in counter.items():
        freqs[count].append(word)

    results = []
    for i in range(len(words), 0, -1):
        if i in freqs:
            for word in freqs[i]:
                results.append((word, i))

        if len(results) >= k:
            break

    results = sorted(results, reverse=True, key=lambda x: x[1])
    return [element[0] for element in results]


if __name__ == "__main__":
    print(
        solution(
            ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], k=2
        )
    )
