"""
Smallest Number that is not a Sum of a Subset of List

This problem was recently asked by AirBNB:

Given a sorted list of positive numbers, 
find the smallest positive number that cannot be a sum of any subset in the list.

Example:
Input: [1, 2, 3, 8, 9, 10]
Output: 7
Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.

"""

def solution(array):
    result = 1

    for number in array:
        if number <= result:
            result += number
        else:
            break
    
    return result


if __name__ == "__main__":
    print(solution([1, 2, 3, 8, 9, 10]))