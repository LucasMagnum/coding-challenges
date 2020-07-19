"""
Product of Array Except Self

This problem was recently asked by Amazon:

You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

"""


def solution(array):
    prefix_products = []
    for num in array:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    suffix_products = []
    for num in reversed(array):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    result = []
    for i in range(len(array)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(array) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    print(solution(array))
