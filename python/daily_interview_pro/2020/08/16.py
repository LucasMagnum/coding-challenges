"""
Maximum Non Adjacent Sum

This problem was recently asked by Google:

Given a list of positive numbers, find the largest possible set such that no elements are adjacent numbers of each other.

"""

def solution(numbers):
    prev_max_sum = 0
    current_max_sum = 0

    for num in numbers:
        t = current_max_sum
        current_max_sum = max(current_max_sum, prev_max_sum + num)
        prev_max_sum = t

    return current_max_sum


if __name__ == "__main__":
    print(solution([3, 4, 1, 1]))
    # 5
    # max sum is 4 (index 1) + 1 (index 3)

    print(solution([2, 1, 2, 7, 3]))
    # 9
    # max sum is 2 (index 0) + 7 (index 3)