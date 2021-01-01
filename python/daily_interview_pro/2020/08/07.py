"""
4 Sum

This problem was recently asked by Microsoft:

Given a list of numbers, and a target number n, find all unique combinations of a, b, c, d, such that a + b + c + d = n.

"""
from collections import defaultdict


def four_sum(nums, target):
    pairs = defaultdict(list)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pairs[nums[i] + nums[j]].append((i, j))

    result = set()

    for p_sum, pairs_list in pairs.items():
        if target - p_sum not in pairs:
            continue

        for pair1 in pairs_list:
            for pair2 in pairs[target - p_sum]:
                if (
                    pair1[0] != pair2[0] and pair1[0] != pair2[1] and
                    pair1[1] != pair2[0] and pair1[1] != pair2[1]
                ):
                    result.add(
                        tuple(sorted([nums[pair1[0]], nums[pair1[1]], nums[pair2[0]], nums[pair2[1]]]))
                    )

    return [list(n) for n in result]



if __name__ == "__main__":
    print(four_sum([1, 1, -1, 0, -2, 1, -1], 0))
    # print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

    print(four_sum([3, 0, 1, -5, 4, 0, -1], 1))
    # print [[-5, -1, 3, 4]]

    print(four_sum([0, 0, 0, 0, 0], 0))
    # print ([0, 0, 0, 0])
