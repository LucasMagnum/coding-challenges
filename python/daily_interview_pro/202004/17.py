"""
Max and Min with Limited Comparisons

This problem was recently asked by Microsoft:

Given a list of numbers of size n, where n is greater than 3, find the 
maximum and minimum of the list using less than 2 * (n - 1) comparisons.

"""

def solution(nums):
    if len(nums) % 2 == 1:
        min_n = max_n = nums[-1]
    else:
        min_n = max_n = nums[0]

    for i in range(len(nums) // 2):
        if nums[2 * i] < nums[2 * i + 1]:
            min_a = nums[2 * i] 
            max_a = nums[2 * i + 1]
        else:
            max_a = nums[2 * i]
            min_a = nums[2 * i + 1]
        
        min_n = min(min_n, min_a)
        max_n = max(max_n, max_a)

    return min_n, max_n

if __name__ == "__main__":
    print(solution([3, 5, 1, 10, 2, 4, 8, 0]))