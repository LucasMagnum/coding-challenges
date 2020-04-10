"""
Min Stack

This problem was recently asked by Uber:

Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Note: be sure that pop() and top() handle being called on an empty stack.

"""


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, x):
        if x < self.min:
            self.min = x

        self.stack.append((x, self.min))

    def pop(self):
        value, _ = self.stack.pop()
        self.min = self.stack[-1][1]
        return value

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.min


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    stack.push(1)
    stack.push(2)

    print(stack.getMin())
    assert stack.getMin() == -3
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.top())
    print(stack.getMin())