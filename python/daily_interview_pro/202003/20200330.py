"""
Reverse Words in a String

This problem was recently asked by Facebook:

Given a string, you need to reverse the order of characters in each word within a 
sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"

Note: In the string, each word is separated by single space and 
there will not be any extra space in the string.

"""


def solution(string):
    words = string.split(" ")

    new_words = []

    for word in words:
        new_words.append(reverse(word))

    return " ".join(new_words)


def reverse(string):
    string = list(string)
    start = 0
    end = len(string) - 1

    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    return "".join(string)


if __name__ == "__main__":
    print(solution("The cat in the hat"))
