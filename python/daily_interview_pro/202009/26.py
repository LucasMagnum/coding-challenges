"""
Closest to 3 Sum

This problem was recently asked by Google:

Given a list of numbers and a target number n,
find 3 numbers in the list that sums closest to the target number n.
There may be multiple ways of creating the sum closest to the target number,
you can return any combination in any order.

"""


def closest_3sum(nums, target):
    nums.sort()
    result = nums[:3]

    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            if abs(target - (nums[i] + nums[r])) < abs(target - sum(result)):
                result = [nums[i], nums[l], nums[r]]

            current_sum = nums[i] + nums[l] + nums[r]
            if current_sum == target:
                return result

            elif current_sum < target:
                l += 1
            else:
                r -= 1

    return result



if __name__ == "__main__":
    print(closest_3sum([2, 1, -5, 4, 3, 6, 7, 2], -1))
    # Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
    # print [-5, 1, 2]