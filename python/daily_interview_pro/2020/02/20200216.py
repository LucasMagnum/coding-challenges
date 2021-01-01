"""
Find Pythagorean Triplets

Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.

print findPythagoreanTriplets([3, 12, 5, 13])
# True

"""
import math
from typing import List


def solution(array: List[int]) -> bool:
    # Construct a doubles set representing the "C" value
    doubles = {number ** 2 for number in array}

    # Check if there is any A and B that is equal to C
    for index, number in enumerate(array):

        for second_number in array[index:]:
            total = (number * number) + (second_number * second_number)

            if total in doubles:
                return True, number, second_number, int(math.sqrt(total))

    return False


if __name__ == "__main__":
    array = [3, 5, 12, 5, 13]
    print(f"Solution({array}) -> ", solution(array))

    array = [1, 2, 4, 6, 7, 8, 33, 56, 65]
    print(f"Solution({array}) -> ", solution(array))
