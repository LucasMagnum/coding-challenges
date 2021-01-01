"""
Rectangle Intersection

This problem was recently asked by LinkedIn:

Given two rectangles, find the area of intersection.

"""


class Rectangle:
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def area(self):
        if self.min_x < self.max_x and self.min_y < self.max_y:
            return (self.max_x - self.min_x) * (self.max_y - self.min_y)
        return 0


def intersection_area(rect1, rect2):
    intersection_rect = Rectangle()
    intersection_rect.min_x = max(rect1.min_x, rect2.min_x)
    intersection_rect.max_x = min(rect1.max_x, rect2.max_x)
    intersection_rect.min_y = max(rect1.min_y, rect2.min_y)
    intersection_rect.max_y = min(rect1.max_y, rect2.max_y)

    return intersection_rect.area()


if __name__ == "__main__":
    #  BBB
    # AXXB
    # AAA
    rect1 = Rectangle(0, 0, 3, 2)
    rect2 = Rectangle(1, 1, 3, 3)
    print(intersection_area(rect1, rect2))
