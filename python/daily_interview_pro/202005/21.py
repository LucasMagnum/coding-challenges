"""
Multitasking

This problem was recently asked by AirBNB:

We have a list of tasks to perform, with a cooldown period.
We can do multiple of these at the same time, but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
tasks = [1, 1, 2, 1]
cooldown = 2

output: 7 (order is 1 _ _ 1 2 _ 1)

"""


def solution(tasks, cooldown):
    last_position = {}

    current = 0

    for task in tasks:
        if task in last_position:
            if current - last_position[task] <= cooldown:
                current = cooldown + last_position[task] + 1
        last_position[task] = current
        current = current + 1

    return current


if __name__ == "__main__":
    print(solution([1, 1, 2, 1], 2))
