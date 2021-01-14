"""
Sort Colors

This problem was recently asked by Apple:

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""

def sort_colors(numbers):
    zidx = 0
    tidx = len(numbers) - 1

    idx = 0
    while idx <= tidx:
        if numbers[idx] == 0:
            numbers[idx], numbers[zidx] = numbers[zidx], numbers[idx]
            zidx += 1
            idx += 1
        elif numbers[idx] == 2:
            numbers[idx], numbers[tidx] = numbers[tidx], numbers[idx]
            tidx -= 1
        else:
            idx += 1

    return numbers


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
    print("Before Sort: ")
    print(nums)
    # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

    sort_colors(nums)
    print("After Sort: ")
    print(nums)
    # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]