"""
Optimized List Sum

his problem was recently asked by Apple:

Create a class that initializes with a list of numbers and has one method called sum. sum should take in two parameters, start_idx and end_idx and return the sum of the list from start_idx (inclusive) to end_idx` (exclusive).

You should optimize for the sum method.

"""


class ListFastSum:
    def __init__(self, nums):
        self.nums = nums
        self.sums = []

        sum_so_far = 0
        for num in self.nums:
            sum_so_far += num
            self.sums.append(sum_so_far)

        self.sums.append(0)

    def sum(self, start_idx, end_idx):
        return self.sums[end_idx - 1] - self.sums[start_idx - 1]


if __name__ == "__main__":
    print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(0, 7))
    # 12 because 3 + 4 + 5 = 12