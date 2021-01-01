"""
Longest Substring Without Repeating Characters

This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

"""

def solution(string):
    letters = {}

    head, tail = 0, -1
    result = 0

    while head < len(string):
        if string[head] in letters:
            tail = max(tail, letters[string[head]])
        letters[string[head]] = head
        result = max(result, head - tail)
        head += 1

    return result


if __name__ == "__main__":
    print(solution("abrkaabcdefghijjxxx"))