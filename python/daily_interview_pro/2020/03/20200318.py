"""
Longest Substring With K Distinct Characters

This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.
"""


def brute_force(string, k):
    current = ""

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]

            if len(set(substring)) <= k and len(substring) > len(current):
                current = substring
    return len(current)


def solution(string, k):
    if k == 0:
        return 0

    bounds = (0, 0)
    mapping = {}

    max_length = 0

    for i, char in enumerate(string):
        mapping[char] = i

        # Determine the lower bound
        if len(mapping) <= k:
            lower_bound = bounds[0]
        else:
            key_to_top = min(mapping, key=mapping.get)
            lower_bound = mapping.pop(key_to_top) + 1

        bounds = (lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length


if __name__ == "__main__":
    string, k = "aabcdeffff", 3
    print(brute_force(string, k))
    print(solution(string, k))
