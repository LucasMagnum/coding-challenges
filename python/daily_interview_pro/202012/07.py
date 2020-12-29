"""
Queue Using Two Stacks

This problem was recently asked by Apple:

Implement a queue class using two stacks.
A queue is a data structure that supports the FIFO protocol
(First in = first out).

Your class should support the enqueue and dequeue methods
like a standard queue.

"""

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if self.s2:
            return self.s2.pop()

        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        return None


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    # 1 2 3