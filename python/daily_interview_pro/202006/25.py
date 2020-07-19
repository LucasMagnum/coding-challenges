"""
Sorted Square Numbers

This problem was recently asked by Microsoft:

Given a list of sorted numbers (can be both negative or positive), return the list of numbers squared in sorted order.

"""


def square_numbers(nums):
    negative_stack = []

    result = []
    for n in nums:
        if n < 0:
            negative_stack.append(n)
            continue

        while len(negative_stack) > 0 and -negative_stack[-1] <= n:
            result.append(negative_stack.pop() ** 2)

        result.append(n ** 2)

    return result


if __name__ == "__main__":
    print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
    # [0, 1, 1, 9, 16, 25, 25]
