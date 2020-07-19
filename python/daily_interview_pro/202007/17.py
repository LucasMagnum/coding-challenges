"""
K Closest Elements

This problem was recently asked by AirBNB:

Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.

"""


def closest_nums(nums, k, x):
    lo = 0
    hi = len(nums)
    mid = (lo + hi) // 2

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] == k:
            break
        elif nums[mid] < k:
            lo = mid
        elif nums[mid] > k:
            hi = mid

    if nums[mid] <= k:
        lower, higher = mid, mid + 1
    else:
        lower, higher = mid - 1, mid

    closest = []
    for _ in range(k):
        if higher >= len(nums) or (lower >= 0 and x - nums[lower] < nums[higher] - x):
            closest.append(nums[lower])
            lower -= 1
        elif higher < len(nums):
            closest.append(nums[higher])
            higher += 1

    return closest


if __name__ == "__main__":
    print(closest_nums([1, 3, 7, 8, 9], 3, 5))
    # [7, 3, 8]
