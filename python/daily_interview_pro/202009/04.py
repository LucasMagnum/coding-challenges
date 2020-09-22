"""
Valid Mountain Array

This problem was recently asked by Microsoft:

Given an array of heights, determine whether the array forms a "mountain" pattern.
A mountain pattern goes up and then down.

Like
  /\
 /  \
/    \
"""


def solution(arr):
    UP = 1
    DOWN = 2
    state = None

    for i in range(1, len(arr)):
        if state is None:
            if arr[i] > arr[i-1]:
                state = UP
                continue
        if state == UP:
            if arr[i] > arr[i-1]:
                continue
            if arr[i] < arr[i-1]:
                state = DOWN
                continue
        if state == DOWN:
            if arr[i] < arr[i-1]:
                continue
        return False
    return state == DOWN


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 1]))
    # True

    print(solution([1, 2, 3]))
    # False