"""
Index of Larger Next Number

This problem was recently asked by Google:

Given a list of numbers, for each element find the next element that is larger than the current element.
Return the answer as a list of indices.
If there are no elements larger than the current element, then use -1 instead.

"""


def larger_number(nums):
    result = [-1] * len(nums)
    stack = []

    for i, n in enumerate(nums):
        while stack and n > nums[stack[-1]]:
            t = stack.pop()
            result[t] = i
        stack.append(i)
    return result


if __name__ == "__main__":
    print(larger_number([3, 2, 5, 6, 9, 8]))
    # print [2, 2, 3, 4, -1, -1]
