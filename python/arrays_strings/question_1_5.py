"""
One Away: 
    There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, 
    write a function to check if they are one edit (or zero edits) away. 
"""
import sys


def solution(first: str, second: str) -> bool:
    first_index = 0
    second_index = 0

    found_difference = False

    shorter, longer = (first, second) if len(first) < len(second) else (second, first)

    while first_index < len(shorter) and second_index < len(longer):
        if shorter[first_index] != longer[second_index]:
            if found_difference:
                return False

            found_difference = True

            if len(shorter) == len(longer):
                first_index += 1
        else:
            first_index += 1

        second_index += 1

    return True


if __name__ == "__main__":
    try:
        first, second = sys.argv[1:]
    except ValueError:
        first, second = "alex", "bale"

    print(f"Solution: ({first}, {second}) => ", solution(first, second))
