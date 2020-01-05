"""
Power Set:
    Write a method to return all subsets of a set.

Ex:
    A = {1, 2}
    [{}, {1}, {2}, {1, 2}]


"""
import time
import sys

def iterative(powerset):
    sets = [[]]

    for value in powerset:
        new_subsets = [subset[:] + [value] for subset in sets]
        sets.extend(new_subsets)

    return sets

def recursive(powerset, index):
    if len(powerset) == index:
        return [[]]
    
    subsets = recursive(powerset, index + 1)
    new_subsets = [[powerset[index]] + subset for subset in subsets]
    subsets.extend(new_subsets)

    return subsets

def binary(powerset):
    subset_size = 1 << len(powerset)  # Compute 2^n 

    subsets = []

    for index in range(0, subset_size):
        subset = convert_to_subset(index, powerset)
        subsets.append(subset)

    return subsets

def convert_to_subset(index, powerset):
    subset = []
    counter = 0

    k = index

    while k > 0:
        if k & 1 == 1:  # K & 1 == 1, K % 2 == 1, odd & even check
            subset.append(powerset[counter])

        k = k >> 1  # K >> 1, K // 2
        counter += 1

    return subset


if __name__ == "__main__":
    powerset = [1, 2, 3]

    start = time.time()
    print(iterative(powerset))
    end = time.time()
    print("iterative took: {:0.4f}".format(end - start))

    start = time.time()
    print(recursive(powerset, 0))
    end = time.time()
    print("recursive took: {:0.4f}".format(end - start))

    start = time.time()
    print(binary(powerset))
    end = time.time()
    print("binary took: {:0.4f}".format(end - start))