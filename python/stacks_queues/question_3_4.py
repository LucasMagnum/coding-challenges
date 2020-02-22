"""
Queue via Stacks:
    Implement a MyQueue class which implements a queue using two stacks.
"""


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def __len__(self):
        return len(self._data)


class Queue:
    def __init__(self):
        self.stack_01 = Stack()
        self.stack_02 = Stack()

    def enqueue(self, item):
        self.stack_01.push(item)

    def dequeue(self):
        if not self.stack_02:
            while self.stack_01:
                self.stack_02.push(self.stack_01.pop())

        return self.stack_02.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
