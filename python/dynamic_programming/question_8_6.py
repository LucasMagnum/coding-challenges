"""
Towers of Hanoi:
    In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different
    sizes which can slide onto another. The puzzle starts with the disks sorted in ascending
    order of size from top to bottom. You have the following constraints:

        * Only one disk can be moved at a time
        * A disk is slid off the top of one tower onto another tower
        * A disk cannot be placed on top of a smaller disk.    

"""
import sys


class Tower:
    def __init__(self, disks=None):
        if not disks:
            disks = []
        self.disks = disks

    def add(self, disk):
        if self.disks and self.disks[-1] <= disk:
            raise ValueError(f"{disk} <= {self.disks[-1]}")
        self.disks.append(disk)

    def move_to_top(self, tower):
        top = self.disks.pop()
        tower.add(top)

    def move_disks(self, quantity, destination, buffer):
        if quantity <= 0:
            return

        self.move_disks(quantity - 1, buffer, destination)
        self.move_to_top(destination)
        buffer.move_disks(quantity - 1, destination, self)


if __name__ == "__main__":
    try:
        N = int(sys.argv[1])
    except IndexError:
        N = 3

    tower_01 = Tower([x for x in range(N, 0, -1)])
    tower_02 = Tower()
    tower_03 = Tower()

    print("Towers in: ", [tower_01.disks, tower_02.disks, tower_03.disks])
    tower_01.move_disks(len(tower_01.disks), tower_03, tower_02)
    print("Towers out: ", [tower_01.disks, tower_02.disks, tower_03.disks])
