"""
Permutations of numbers

This problem was recently asked by Facebook:

You are given an array of integers.
Return all the permutations of this array.

"""

def permute(nums):
    results = [[]]

    for value in nums:
        temp = []

        for result in results:
            size = len(result)

            for idx in range(size + 1):
                result_copy = result[:]
                result_copy.insert(idx, value)
                temp.append(result_copy)

        results = temp

    return results


def recursive(nums):
    if len(nums) == 1:
        return [nums]

    output = []
    for value in recursive(nums[1:]):
        for idx in range(len(nums)):
            output.append(value[:idx] + [nums[0]] + value[idx:])
    return output

if __name__ == "__main__":
    print(permute([1, 2, 3]))
    print(recursive([1, 2, 3]))
    # [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
