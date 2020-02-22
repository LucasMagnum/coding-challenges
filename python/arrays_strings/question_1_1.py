"""
    Is Unique:
         Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
import sys


def brute_force_solution(string):
    """
    Check each character with all the remaining ones.
    """
    for index, character in enumerate(string):
        for another_character in string[index + 1 :]:
            if character == another_character:
                return False
    return True


def count_solution(string):
    """Keep tracks of the seen characters."""
    counter = {}

    for character in string:
        if character in counter:
            return False
        counter[character] = True

    return True


def bit_array_solution(string):
    """
    Create a bit array and uses it to toggle a character based on its number.
    """
    checker = 0

    for character in string:
        value = ord(character) - ord("a")
        if checker & (1 << value) > 0:
            return False
        checker |= 1 << value
    return True


if __name__ == "__main__":
    try:
        string = sys.argv[1]
    except IndexError:
        string = "Lucas"

    print("Brute force: ", brute_force_solution(string))
    print("Counting: ", count_solution(string))
    print("Bit Array: ", bit_array_solution(string))
