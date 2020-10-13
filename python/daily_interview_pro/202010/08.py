"""
Generate all subsets

This problem was recently asked by Facebook:

Given a list of unique numbers, generate all possible subsets without duplicates.
This includes the empty set as well.
"""


def generateAllSubsets(nums):
    subsets = [[]]

    for num in nums:
        temp = []
        for subset in subsets:
            temp.append(subset)
            temp.append([*subset, num])

        subsets = temp

    return subsets


if __name__ == "__main__":
    print(generateAllSubsets([1, 2, 3]))
    # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]