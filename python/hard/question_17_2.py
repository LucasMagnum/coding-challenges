"""
    Shuffle:
        Write a method to shuffle a deck of cards. It must be a perfect shuffle - in other words, each of the 52! permutations of the
        deck has to be equally likely. Assume that you are given a random number generator which is perfect.
"""
import random
from typing import List


def solution(deck: List[int]) -> List[int]:
    for index in range(len(deck) - 1):
        new_position = random.randint(0, index + 1)
        deck[index], deck[new_position] = deck[new_position], deck[index]
    return deck


def recursive(deck: List[int], index: int) -> List[int]:
    if index == 0:
        return deck
    
    recursive(deck, index - 1)
    new_position = random.randint(0, index + 1)
    deck[index], deck[new_position] = deck[new_position], deck[index]

    return deck


if __name__ == "__main__":
    deck = list(range(1, 53))

    print("Solution: ", solution(deck))
    assert sorted(deck) == list(range(1, 53))

    print("Solution: ", recursive(deck, len(deck) - 1))
    assert sorted(deck) == list(range(1, 53))