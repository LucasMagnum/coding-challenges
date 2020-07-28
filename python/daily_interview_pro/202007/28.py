"""
Intersection of Lists

This problem was recently asked by Twitter:

Given 3 sorted lists, find the intersection of those 3 lists.

"""


def intersection(list1, list2, list3):
    idx1 = idx2 = idx3 = 0

    result = []
    while idx1 < len(list1) and idx2 < len(list2) and idx3 < len(list3):
        if list1[idx1] == list2[idx2] == list3[idx3]:
            result.append(list1[idx1])
            idx1 += 1
            idx2 += 1
            idx3 += 1
            continue

        max_num = max(list1[idx1], list2[idx2], list3[idx3])

        if list1[idx1] < max_num:
            idx1 += 1

        if list2[idx2] < max_num:
            idx2 += 1

        if list3[idx3] < max_num:
            idx3 += 1

    return result

if __name__ == "__main__":
    print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
    # [4]
