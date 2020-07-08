"""
This problem was recently asked by Amazon:

A task is a some work to be done which can be assumed takes 1 unit of time.
Between the same type of tasks you must take at least n units of time before running the same tasks again.

Given a list of tasks (each task will be represented by a string),
and a positive integer n representing the time it takes to run the same task again,
find the minimum amount of time needed to run all tasks.
"""
import heapq
from collections import defaultdict


def schedule_tasks(tasks, n):
    task_counter = defaultdict(int)
    for task in tasks:
        task_counter[task] += 1

    pq = []
    for task, count in task_counter.items():
        heapq.heappush(pq, (-count, task))

    time = 0

    while pq:
        add_back = []
        for _ in range(n):
            if pq:
                if -pq[0][0] > 1:
                    task_count = heapq.heappop(pq)
                    add_back.append((task_count[0] + 1, task_count[1]))
                else:
                    heapq.heappop(pq)
            time += 1
            if not pq and not add_back:
                break

        for x in add_back:
            heapq.heappush(pq, x)
    return time


if __name__ == "__main__":
    print(schedule_tasks(['q', 'q', 's', 'q', 'w', 'w'], 4))
    # print 6
    # one of the possible orders to run the task would be
    # 'q', 'w', idle, idle, 'q', 'w'