import sys


def binary_search(array, item, start, end):
    if end < start:
        return -1
    
    mid = (start + end) // 2

    if item == array[mid]:
        return mid

    if item > array[mid]:
        return binary_search(array, item, mid + 1, end)
    return binary_search(array, item, start, mid - 1)


def binary_search_iterative(array, item):
    start, end = 0, len(array) - 1

    while end >= start:
        mid = (start + end) // 2

        if array[mid] == item:
            return mid

        start, end = (mid + 1, end) if item > array[mid] else (start, mid - 1)

    return -1 


if __name__ == "__main__":
    try:
        item = int(sys.argv[1])
    except (IndexError, ValueError):
        item = 2

    print(binary_search([1, 2, 3, 5, 6, 7, 9], item, 0, 6))
    print(binary_search_iterative([1, 2, 3, 5, 6, 7, 9], item))