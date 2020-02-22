"""
Three in One:
    Describe how you could use a single array to implement three stacks.
"""

class Stack:
    def __init__(self, array, start, end):
        self.array = array
        self.start = start
        self.current = start
        self.end = end

    def push(self, value):
        if self.current == self.end:
            raise ValueError("Stack is full")
        self.array[self.current] = value
        self.current += 1

    def pop(self):
        if self.current < self.start:
            raise ValueError("Stack is empty")
        value = self.array[self.current - 1]
        self.array[self.current - 1] = None
        self.current -= 1
        return value

    def top(self):
        return self.array[self.current - 1]


def solution(array):
    size = len(array)
    size_stack = size // 3

    stack_01 = Stack(array, 0, size_stack)
    stack_02 = Stack(array, size_stack, size_stack + size_stack)
    stack_03 = Stack(array, size_stack + size_stack, size)

    for x in range(0, 10):
        stack_01.push(x)

    for x in range(10, 20):
        stack_02.push(x)

    for x in range(20, 30):
        stack_03.push(x)

    for x in range(29, 20, -1):
        value = stack_03.pop()
        assert value == x, f"{x} != {value}"

    for x in range(19, 10, -1):
        value = stack_02.pop()
        assert value == x, f"{x} != {value}"

    for x in range(9, 0, -1):
        value = stack_01.pop()
        assert value == x, f"{x} != {value}"

    print(array)


if __name__ == "__main__":
    array = [None] *  30
    print("Solution: ", solution(array))