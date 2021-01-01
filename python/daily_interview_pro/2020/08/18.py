"""
Generate all subsets

This problem was recently asked by Facebook:

Given a list of unique numbers, generate all possible subsets without duplicates. This includes the empty set as well.

"""


def solution(nums):
    result = [[]]

    for num in nums:
        temp = []
        for x in result:
            temp.append(x)
            temp.append([*x, num])
        result = temp
    return result


if __name__ == "__main__":
    print(solution([1, 2, 3]))
    # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]