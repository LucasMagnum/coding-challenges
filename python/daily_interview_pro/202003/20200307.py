"""
Queue Using Two Stacks


This problem was recently asked by Apple:

Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.

"""


class Queue:
    def __init__(self):
        self.stack_01 = []
        self.stack_02 = []

    def enqueue(self, val):
        self.stack_01.append(val)

    def dequeue(self):
        if not self.stack_02:
            while self.stack_01:
                self.stack_02.append(self.stack_01.pop())

        return self.stack_02.pop()


if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
