"""
Animal Shelter

An animal shelter, which holds only dogs and cats, operates in a strictly "first in, first out" basis.
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or
they can selet whether they would prefer a dog or a cat (and will recieve the oldest animal of that
type).

They cannot select which specific animal they would like. Create the data structures to maintain this system
and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the
built-in LinkedList data structure.
"""


from dataclasses import dataclass
from collections import deque


@dataclass
class Animal:
    name: str
    order: int = 0


class Cat(Animal):
    pass


class Dog(Animal):
    pass


@dataclass
class Node:
    value: str
    next: "Node"


class AnimalShelter:
    """This is my implementation of the animal shelter"""

    def __init__(self):
        self.head = None
        self.current = None

    def enqueue(self, animal: Animal):
        node = Node(animal, None)

        if not self.head:
            self.head = node
            self.current = node
        else:
            self.current.next = node
            self.current = node

    def dequeue_cat(self) -> Cat:
        return self.dequeue(Cat)

    def dequeue_dog(self) -> Dog:
        return self.dequeue(Dog)

    def dequeue(self, animal_type=None) -> Animal:
        if not self.head:
            raise ValueError("Shelter is empty")

        value = self.head
        prev = None

        if animal_type:
            while not isinstance(value.value, animal_type):
                prev = value
                value = value.next

        if prev:
            prev.next = value.next
        else:
            self.head = self.head.next

        value.next = None
        return value


class BookAnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1

        if isinstance(animal, Dog):
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

    def dequeue(self):
        if not self.dogs:
            return self.dequeue_cat()
        elif not self.cats:
            return self.dequeue_dog()

        cat = self.cats[0]
        dog = self.dogs[0]

        if dog.order > cat.order:
            return self.dequeue_cat()
        else:
            return self.dequeue_dog()

    def dequeue_cat(self):
        return self.cats.popleft()

    def dequeue_dog(self):
        return self.dogs.popleft()


if __name__ == "__main__":
    shelter = BookAnimalShelter()
    shelter.enqueue(Cat("Thunder"))
    shelter.enqueue(Dog("Lala"))
    shelter.enqueue(Cat("Inácio"))
    shelter.enqueue(Dog("Tove"))

    print(shelter.dequeue())
    print(shelter.dequeue_dog())
    print(shelter.dequeue_cat())

    shelter.enqueue(Dog("Dog"))

    print(shelter.dequeue())
