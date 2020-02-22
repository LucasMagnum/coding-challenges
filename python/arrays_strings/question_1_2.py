"""
    Check permutation:
        Given two strings, write a method to decide if one is a permutation of the
        other.
"""
import itertools
import sys


def brute_force(first: str, second: str) -> bool:
    """Brute force solution checking if there's a permutation
    equal to the value."""
    if len(first) != len(second):
        return False

    permutations = itertools.permutations(first)
    second = tuple(second)

    for permutation in permutations:
        if permutation == second:
            return True

    return False


def solution(first: str, second: str) -> bool:
    """Counting the characters solution.
    A permutation will have the same amount of characters."""
    if len(first) != len(second):
        return False

    counter = {}

    for character in first:
        counter[character] = counter.get(character, 0) + 1

    for character in second:
        count = counter.get(character, 0)
        if count - 1 < 0:
            return False
        counter[character] = count - 1

    for k, v in counter.items():
        if v != 0:
            return False

    return True


def sorting_solution(first: str, second: str) -> True:
    """Sort both strings and check each character."""
    if len(first) != len(second):
        return False

    first = sorted(first)
    second = sorted(first)

    for index in range(len(first)):
        if first[index] != second[index]:
            return False
    return True


def binary_solution(first: str, second: str) -> True:
    checker = 0

    if len(first) != len(second):
        return False

    for character in first:
        checker ^= ord(character)

    for character in second:
        checker ^= ord(character)

    return checker == 0


if __name__ == "__main__":
    try:
        first, second = sys.argv[1:]
    except ValueError:
        first, second = ("god", "dog")

    print(f"Solution: ({first}, {second}): ", solution(first, second))
    print(f"Solution (sorting): ({first}, {second}): ", sorting_solution(first, second))
    print(f"Brute force: ({first}, {second}): ", brute_force(first, second))
    print(f"Binary solution: ({first}, {second}): ", binary_solution(first, second))