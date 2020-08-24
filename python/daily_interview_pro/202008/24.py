"""
Find the K-th Largest Number

This problem was recently asked by Twitter:

Find the k-th largest number in a sequence of unsorted numbers.

"""


def quick_select(array, k):
    k = len(array) - k
    left = 0
    right = len(array) - 1

    while left <= right:
        pivot = partition(array, left, right)
        if pivot == k:
            return array[pivot]
        elif pivot > k:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


def partition(array, low, high):
    pivot = array[high]
    i = low

    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[high] = array[high], array[i]
    return i


if __name__ == "__main__":
    print(quick_select([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))