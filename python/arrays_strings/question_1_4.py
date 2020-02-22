"""
Palindrome Permutation: 
    Given a string, write a function to check if it is a permutation of
    a palindrome. A palindrome is a word or phrase that is the same forwards and backwards, A
    permutation is a rearrangement of letters. The palindrome does not need to be limited to just
    dictionary words. 

    Ex: Tact Coa
"""
import sys


def solution(string: str) -> bool:
    counter = {}

    for character in string:
        if not character.strip():
            continue

        counter[character] = counter.get(character, 0) + 1

    odd_count = 0

    for character, count in counter.items():
        if count % 2 != 0:
            odd_count += 1

        if odd_count > 1:
            return False

    return True


if __name__ == "__main__":
    try:
        string = " ".join(sys.argv[1:])
    except IndexError:
        string = "Tact Coa"

    print(f"Solution: ({string})", solution(string.lower()))
