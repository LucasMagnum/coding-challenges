"""
    Stack of Boxes:

    You have a stack of n boxes, with widths w , heights h,and depths d. The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. 

Implement a method to compute the height of the tallest possible stack. 
The height of a stack is the sum of the heights of each box.     
"""
import random


def brute_force_solution(boxes):
    boxes = sorted(boxes, key=lambda item: item["width"])

    max_height = 0

    for index, box in enumerate(boxes):
        height = calculate_height(boxes, index)
        max_height = max([max_height, height])

    return max_height


def calculate_height(boxes, bottom_index):
    bottom_box = boxes[bottom_index]
    max_height = 0

    for index, box in enumerate(boxes[bottom_index + 1:], bottom_index + 1):
        if can_be_above(box, bottom_box):
            height = calculate_height(boxes, index)
            max_height = max([max_height, height])

    max_height += bottom_box["height"]
    return max_height


def memoization(boxes):
    boxes = sorted(boxes, key=lambda item: item["width"])

    max_height = 0

    cache = {}

    for index, box in enumerate(boxes):
        height = calculate_height_cache(boxes, index, cache)
        max_height = max([max_height, height])

    return max_height


def calculate_height_cache(boxes, bottom_index, cache):
    if bottom_index < len(boxes) and cache.get(bottom_index, 0) > 0:
        return cache[bottom_index]

    bottom_box = boxes[bottom_index]
    max_height = 0

    for index, box in enumerate(boxes[bottom_index + 1:], bottom_index + 1):
        if can_be_above(box, bottom_box):
            height = calculate_height_cache(boxes, index, cache)
            max_height = max([max_height, height])

    max_height += bottom_box["height"]
    cache[bottom_index] = max_height
    return max_height


def choice_algorithm(boxes):
    boxes = sorted(boxes, key=lambda item: item["width"])
    cache = {}
    return get_maximium_height(boxes, None, 0, cache)


def get_maximium_height(boxes, bottom_box, box_index, cache):
    if box_index >= len(boxes):
        return 0
    
    new_bottom = boxes[box_index]
    height_with_bottom = 0

    if bottom_box is None or can_be_above(new_bottom, bottom_box):
        if cache.get(box_index, 0) == 0:
            cache[box_index] = get_maximium_height(boxes, new_bottom, box_index + 1, cache) 
            cache[box_index] += new_bottom["height"]
        height_with_bottom = cache[box_index]

    # Without this bottom
    height_without_bottom = get_maximium_height(boxes, bottom_box, box_index + 1, cache)

    # Return better of two options
    return max([height_with_bottom, height_without_bottom])


def can_be_above(box, bottom_box):
    conditions = [
        box["width"] > bottom_box["width"],
        box["height"] > bottom_box["height"],
        box["depth"] > bottom_box["depth"]
    ]

    return all(conditions)


if __name__ == "__main__":
    positions = list(range(20))
    random.shuffle(positions)

    boxes = [{"width": x, "height": x, "depth": x} for x in positions]

    print("Solution (brute force): ", brute_force_solution(boxes))
    print("Solution (memoization): ", memoization(boxes))
    print("Solution (choice algorithm): ", choice_algorithm(boxes))