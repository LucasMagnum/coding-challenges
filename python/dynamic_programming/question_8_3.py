"""
Magic Index:
    A magic index is an array A[0...N-1] is defined to be an index
    such that A[i] == i.

    Given a sorted array of distinct integers, write a method to find 
    a magic index, if one exists, in array A.

    What if the values are not distinct?
"""
import random
import sys


def brute_force(array):
    for index, value in enumerate(array):
        if index == value:
            return index
    return -1 


def magic_fast_distinct(array, start, end):
    if end < start:
        return -1 
    
    middle = (end + start) // 2
    if array[middle] == middle:
        return middle
    
    start, end = (middle + 1, end) if middle > array[middle] else (start, middle - 1)
    return magic_fast_distinct(array, start, end)


def magic_fast_not_distinct(array, start, end):
    if end < start:
        return -1
    
    middle = (end + start) // 2
    middle_value = array[middle]
    if middle_value == middle:
        return middle

    left_index = min([middle - 1, array[middle]])
    left = magic_fast_not_distinct(array, start, left_index)
    if left >= 0:
        return left
    
    right_index = max([middle + 1, middle_value])
    right = magic_fast_not_distinct(array, right_index, end)

    return right
    

if __name__ == "__main__":
    import time
    N = int(sys.argv[1])

    array = [random.randint(-N//4, N) for _ in range(0, N)]
    array = sorted(array)

    start = time.time()
    print(brute_force(array))
    end = time.time()
    print("Brute force solution - Took: {:.3f}".format(end - start))

    start = time.time()
    print(magic_fast_distinct(array, 0, N - 1))
    end = time.time()
    print("Distinct solution - Took: {:.3f}".format(end - start))

    start = time.time()
    print(magic_fast_not_distinct(array, 0, N - 1))
    end = time.time()
    print("Not distinct solution - Took: {:.3f}".format(end - start))
