"""
Multitasking

This problem was recently asked by AirBNB:

We have a list of tasks to perform, with a cooldown period.
We can do multiple of these at the same time, but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks
in the order they are input.

tasks = [1, 1, 2, 1]
cooldown = 2

output: 7 (order is 1 _ _ 1 2 _ 1)

"""


def findTime(tasks, cooldown):
    last_pos = {}
    current = 0

    for task in tasks:
        if task in last_pos:
            if current - last_pos[task] <= cooldown:
                current = cooldown + last_pos[task] + 1

        last_pos[task] = current
        current += 1

    return current


if __name__ == "__main__":
    print(findTime([1, 1, 2, 1], 2))
    # 7
