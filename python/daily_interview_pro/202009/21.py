"""
Minimum Size Subarray Sum

This problem was recently asked by Amazon:

Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""

def solution(nums, s):
    l, r = 0, -1

    total = 0
    result = len(nums) + 1

    while l < len(nums):
        if total < s and r + 1 < len(nums):
            # if sum is smaller, keep moving right index to increase window
            r += 1
            total += nums[r]
        else:
            total -= nums[l]
            l += 1

        if total >= s:
            # if sum is found
            result = min(result, r - l + 1)

    if result == len(nums) + 1:
        # if no solution is found
        return 0

    return result

if __name__ == "__main__":
    print(solution([2, 3, 1, 2, 4, 3], 7))
    # 2