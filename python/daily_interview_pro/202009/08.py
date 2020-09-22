"""
Array of equal parts

This problem was recently asked by Twitter:

Given an array containing only positive integers,
return if you can pick two integers from the array which cuts the array into
 three pieces such that the sum of elements in all pieces is equal.

Example 1:
Input: array = [2, 4, 5, 3, 3, 9, 2, 2, 2]

Output: true
Explanation: choosing the number 5 and 9 results in three pieces [2, 4], [3, 3] and [2, 2, 2]. Sum = 6.

Example 2:
Input: array =[1, 1, 1, 1],

Output: false

"""

def solution(array):
    if len(array) < 5:
        return False

    total_sum = sum(array)
    left_index = 1
    right_index = len(array) - 2

    left_sum = array[0]
    right_sum = array[-1]

    while left_index < right_index - 1:
        if left_sum < right_sum:
            left_sum += array[left_index]
            left_index += 1

        elif left_sum > right_sum:
            right_sum += array[right_index]
            right_index -= 1

        else:
            mid_sum = total_sum - left_sum - right_sum - array[left_index] - array[right_index]

            if mid_sum < left_sum:
                return False

            elif mid_sum > left_sum:
                left_sum += array[left_index]
                right_sum += array[right_index]

                left_index += 1
                right_index -= 1

            else:
                return True

    return False


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 3, 9, 2, 2, 2])) # True
    print(solution([1, 2, 3, 4, 5])) # False


