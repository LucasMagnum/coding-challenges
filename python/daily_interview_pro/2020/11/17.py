"""
Maximum In A Stack

This problem was recently asked by Twitter:

Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.


"""


class MaxStack:
    def __init__(self):
        self.data = []
        self.max_value = float("-inf")

    def push(self, val):
        if val > self.max_value:
            self.max_value = val

        self.data.append((val, self.max_value))

    def pop(self):
        val, _ = self.data.pop()
        return val

    def max(self):
        return self.data[-1][1]


if __name__ == "__main__":
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)

    assert s.max() == 3

    s.pop()
    s.pop()
    assert s.max() == 2