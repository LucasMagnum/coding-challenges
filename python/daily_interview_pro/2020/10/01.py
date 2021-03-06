"""
Trapping Rainwater

This problem was recently asked by Uber:

You have a landscape, in which puddles can form.
You are given an array of non-negative integers representing the elevation at each location.
Return the amount of water that would accumulate if it rains.

For example:  [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
       X
   X███XX█X
 X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]

"""


def capacity(array):
    array_size = len(array)
    left_maxes = [0 for _ in range(array_size)]
    right_maxes = [0 for _ in range(array_size)]

    current_left_max = 0
    for i in range(array_size):
        current_left_max = max(current_left_max, array[i])
        left_maxes[i] = current_left_max

    current_right_max = 0
    for i in range(array_size - 1, -1, -1):
        current_right_max = max(current_right_max, array[i])
        right_maxes[i] = current_right_max

    total = 0
    for i in range(array_size):
        total += min(left_maxes[i], right_maxes[i]) - array[i]
    return total


if __name__ == "__main__":
    print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 0, 2, 1]))
    # 6
