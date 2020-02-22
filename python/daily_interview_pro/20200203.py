"""
Longest Substring Without Repeating Characters

This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

"""


def solution(string: str) -> int:
    letters = {}

    tail, head = -1, 0
    result = 0

    while head < len(string):
        letter = string[head]

        if letter in letters:
            tail = max(tail, letters[letter])

        letters[letter] = head

        result = max(result, head - tail)
        head += 1

    return result


if __name__ == "__main__":
    string = "lucasmagnumlopesoliveira"
    print(f"Solution({string}) -> ", solution(string))
