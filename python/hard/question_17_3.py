"""
Random Set:
    Write a method to randomly generate a set of M integers from an array of size n. 
    Each element must have equal probability of being chosen.
"""
import random
from typing import List


def solution(array: List[int], total: int) -> List[int]:
    if total > len(array):
        return 
    
    subset = array[:total]

    for index in range(total, len(array) - 1):
        random_position = random.randint(0, index + 1)
        
        if random_position < total:
            subset[random_position] = array[index]
    
    return subset


if __name__ == "__main__":
    array = list(range(1, 53))

    print("Solution: ", solution(array, 10))