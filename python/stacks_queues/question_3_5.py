"""
Sort Stack:

    Write a program to sort a stack such that the smallest items are on the top.
    You can use an additional temporary stack, but you may not copy the elements into any
    other data structure (such as an array).

    The stack supports the following operations: push, pop, peek, and isEmpty.
"""

import random


class Stack:
    def __init__(self):
        self._data = []

    def __str__(self):
        return repr(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def __len__(self):
        return len(self._data)


def solution(stack):
    temp_stack = Stack()

    while stack:
        tmp = stack.pop()

        while temp_stack and temp_stack.peek() > tmp:
            stack.push(temp_stack.pop())

        temp_stack.push(tmp)

    while temp_stack:
        stack.push(temp_stack.pop())

    return stack


if __name__ == "__main__":
    stack = Stack()
    for _ in range(10):
        stack.push(random.randint(0, 100))

    print(f"Solution({stack}", solution(stack))