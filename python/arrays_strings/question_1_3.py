"""
URLify

    Write a method to replace all spaces in a string with %20. You may assume that
    the string has sufficient space at the end to hold additional characters, and
    that you are given the "true" length of the string.

    Ex:
        > "Mr John Smith    ", 13
        "Mr%20John%20Smith"
"""


def solution(string: str, size: int) -> str:
    string_copy = list(string)

    original_index = 0
    second_index = 0

    while original_index < size:
        if string[original_index] != " ":
            string_copy[second_index] = string[original_index]
            second_index += 1
        else:
            string_copy[second_index] = "%"
            string_copy[second_index + 1] = "2"
            string_copy[second_index + 2] = "0"
            second_index += 3

        original_index += 1

    return "".join(string_copy)


if __name__ == "__main__":
    string, size = "Mr John Smith    ", 13
    print("Solution({string}) ->", solution(string, size))