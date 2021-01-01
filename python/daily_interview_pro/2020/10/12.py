"""
Subarray With Target Sum

This problem was recently asked by Amazon:

You are given an array of integers, and an integer K.
Return the subarray which sums to K.
You can assume that a solution will always exist.


"""


def find_continuous_k(array, k):
    left, right = 0, 0
    current_sum = 0

    while left < len(array) or right < len(array):
        if current_sum == k:
            return array[left: right]

        if current_sum < k:
            current_sum += array[right]
            right += 1
        else:
            current_sum -= array[left]
            left += 1

    return -1



if __name__ == "__main__":
    print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
    # [2, 5, 7]
