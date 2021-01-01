"""
Longest Consecutive Sequence

This problem was recently asked by Amazon:

You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.

"""


def sorted_solution(array):
    sorted_array = sorted(array)
    count = 1
    longest = 1

    for i in range(len(array) - 1):
        if sorted_array[i + 1] - sorted_array[i] == 1:
            count += 1
            longest = max(longest, count)

    return longest


def solution(array):
    max_len = 0
    bounds = dict()

    for number in array:
        if number in bounds:
            continue

        left_bound, right_bound = number, number

        if number - 1 in bounds:
            left_bound = bounds[number - 1][0]
        if number + 1 in bounds:
            right_bound = bounds[number + 1][1]

        bounds[number] = left_bound, right_bound
        bounds[left_bound] = left_bound, right_bound
        bounds[right_bound] = left_bound, right_bound
        max_len = max(right_bound - left_bound + 1, max_len)

    return max_len


if __name__ == "__main__":
    print(sorted_solution([100, 4, 200, 1, 3, 2]))
    print(solution([100, 4, 200, 1, 3, 2]))
