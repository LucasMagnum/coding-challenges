"""
    Stack of Plates: 
    
    Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
    threshold. Implement a data structure SetOfStack s that mimics this. SetOfStack s should be
    composed of several stacks and should create a new stack once the previous one exceeds capacity,
    SetOfStacks . push() and SetOfStacks.pop O should behave identically to a single stack
    (that is, pop() should return the same values as it would if there were just a single stack).
    FOLLOW UP
    Implement a function popAt (in t index ) which performs a pop operation on a specific substack
"""


class SetOfStacks:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_stack = []
        self.stacks = [self.current_stack]

    def push(self, item):
        if len(self.current_stack) == self.max_size:
            self.current_stack = []
            self.stacks.append(self.current_stack)

        self.current_stack.append(item)

    def pop(self, stack_index=None):
        if stack_index is not None:
            return self.stacks[stack_index].pop()
        return self.current_stack.pop()

    def __len__(self):
        return sum([len(stack) for stack in self.stacks])


if __name__ == "__main__":
    stack = SetOfStacks(max_size=25)

    for x in range(1, 101):
        stack.push(x)

    assert len(stack) == 100
    assert stack.pop() == 100
    assert stack.pop(0) == 25
