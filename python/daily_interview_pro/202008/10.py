"""
Unique Sum Combinations

This problem was recently asked by Twitter:

Given a list of numbers and a target number, find all possible unique subsets of the list of numbers that sum up to the target number.
The numbers will all be positive numbers.

"""

def sum_combinations(nums, target):
  results = set()
  nums.sort()

  backtrack(nums, 0, target, (), results)
  return list(results)

def backtrack(nums, curr_idx, target, combination, results):
    if target == 0:
        results.add(combination)
        return
    if target < 0:
        return

    for idx in range(curr_idx, len(nums)):
        backtrack(nums, idx + 1, target -
                nums[idx], (*combination, nums[idx]), results)


if __name__ == "__main__":
    print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
    # [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]