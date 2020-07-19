"""
No Adjacent Repeating Characters

This problem was recently asked by LinkedIn:

Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement is possible, then return None.

Example:
Input: abbccc
Output: cbcbca
"""

from collections import defaultdict
import heapq


def rearrangeString(s):
    frequency = defaultdict(int)

    for c in s:
        frequency[c] += 1

    most_freq = []
    for char, count in frequency.items():
        heapq.heappush(most_freq, (-count, char))

    curr_char = heapq.heappop(most_freq)
    final = [curr_char[1]]

    while most_freq:
        new_char = heapq.heappop(most_freq)
        final.append(new_char[1])

        if -curr_char[0] > 1:
            heapq.heappush(most_freq, (curr_char[0] + 1, curr_char[1]))
        curr_char = new_char

    if -curr_char[0] > 1:
        return None

    return "".join(final)


if __name__ == "__main__":
    print(rearrangeString("abbccc"))
