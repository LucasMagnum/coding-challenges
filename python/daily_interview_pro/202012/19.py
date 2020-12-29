"""
Find the K-th Largest Number

This problem was recently asked by Twitter:

Find the k-th largest number in a sequence of unsorted numbers.

"""

def quickselect(arr, k):
    k = len(arr) - k
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = partition(arr, left, right)
        if pivot == k:
            return arr[pivot]
        elif pivot > k:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


if __name__ == "__main__":
    print(quickselect([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))