"""
Find Duplicates

This problem was recently asked by Amazon:

Given an array of size n, and all values in the array are in the range 1 to n, find all the duplicates.

"""


def solution(array):
    output = []

    for number in array:
        value = abs(number) - 1
        if array[value] < 0:
            output.append(abs(number))
        else:
            array[value] = array[value] * -1

    return output


if __name__ == "__main__":
    print(solution([4,3,2,7,8,2,3,1]))