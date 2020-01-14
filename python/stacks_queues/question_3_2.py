"""
Stack min   : 
    How would you design a stack which, in addition to push and pop,
    has a function min which returns the minimum element? 
    Push, pop and min should all operate in 0(1) time. 
"""

class Stack:
    """
    This implementation keeps track at the min value each time
    a value is inserted in the stack.

    This can be inefficient when having a large stack.
    """
    def __init__(self):
        self._data = []
        self.min_value = float("inf")

    def push(self, item):
        self.min_value = min([item, self.min_value])
        self._data.append((item, self.min_value))

    def pop(self):
        item, _ = self._data.pop()
        return item

    def min(self):
        _, min_value = self._data[-1]
        return min_value


class StackWithMin:
    """
    This stack uses another stack to keep track of its values.
    """
    def __init__(self):
        self._data = []
        self._min_values = []

    def push(self, item):
        if not self._min_values or self.min() >= item:
            self._min_values.append(item)
        self._data.append(item)

    def pop(self):
        item = self._data.pop()
        if item == self.min():
            self._min_values.pop()
        return item

    def min(self):
        return self._min_values[-1]

if __name__ == "__main__":
    stacks = [Stack, StackWithMin]

    for stack_klass in stacks:
        stack = stack_klass()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.pop() == 2

        stack.push(5)
        stack.push(0)

        assert stack.min() == 0
        assert stack.pop() == 0
        assert stack.min() == 1

    print("Working as expected!")