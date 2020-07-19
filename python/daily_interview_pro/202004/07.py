"""
Distribute Bonuses

This problem was recently asked by Twitter:

You are the manager of a number of employees who all sit in a row. The CEO would like to give bonuses to all of your employees, but since the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.

The rules of giving bonuses is that:
- Each employee begins with a bonus factor of 1x.
- For each employee, if they perform better than the person sitting next to them, the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).

Given a list of employee's performance, find the bonuses each employee should get.

Example:
Input: [1, 2, 3, 2, 3, 5, 1]
Output: [1, 2, 3, 1, 2, 3, 1]
"""


def solution(array):
    bonus = [1] * len(array)

    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            bonus[i] = bonus[i - 1] + 1

    for i in range(len(bonus) - 2, -1, -1):
        if array[i + 1] < array[i]:
            bonus[i] = max(bonus[i], bonus[i + 1] + 1)

    return bonus


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3, 5, 1]))
