"""
Valid Mountain Array

This problem was recently asked by Microsoft:

Given an array of heights, determine whether the array forms a "mountain" pattern. A mountain pattern goes up and then down.

Like
  /\
 /  \
/    \

"""


def solution(array):
    left, right = 0, len(array) - 1

    while left < right:
        if array[left] > array[left + 1]:
            return False

        if array[right] > array[right - 1]:
            return False

        left += 1
        right -= 1

    return True


print(solution([1, 2, 3, 2, 1]))
# True

print(solution([1, 2, 3]))
# False