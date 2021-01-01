"""
Reverse words

This problem was recently asked by Apple:

Given a list of words in a string, reverse the words in-place
(ie don't create a new string and reverse the words).

Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).

"""


def solution(words):
    reverse(words, 0, len(words))

    start = 0
    idx = 0

    while idx < len(words):
        if words[idx] == " ":
            reverse(words, start, idx)

            while idx + 1 < len(words) and words[idx + 1] == " ":
                idx += 1

            start = idx + 1
        idx += 1

    reverse(words, start, len(words))


def reverse(s, start, end):
    for i in range(0, (end - start) // 2):
        s[start + i], s[end - i - 1] = s[end - i - 1], s[start + i]


if __name__ == "__main__":
    words = list("can you read this")
    solution(words)
    print("".join(words))
