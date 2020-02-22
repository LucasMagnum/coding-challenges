"""
String Rotation; 
    Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
    call to isSubstring [e.g., "waterbottle" is a rotation of erbottlewat"], 
"""
import sys


def solution(first: str, second: str) -> True:
    if len(first) != len(second):
        return False

    composed_string = "".join([first, first])
    return composed_string.find(second) != -1


if __name__ == "__main__":
    try:
        first, second = sys.argv[1:]
    except IndexError:
        first, second = "lucas", "caslu"

    print(f"Solution: ({first}, {second}) ", solution(first, second))
