"""
This problem was recently asked by Amazon:

Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.

"""

def solution(array_01, array_02):
    values = {}
    duplicates = {}

    for value in array_01:
        values[value] = 1
    
    for value in array_02:
        if value in values:
            duplicates[value] = 1
        
    return [key for key in duplicates]


if __name__ == "__main__":
    array_01 = [1, 2, 2, 1]
    array_02 = [2, 2]

    assert solution(array_01, array_02) == [2]
    print(solution(array_01, array_02))

    array_01 = [4, 9, 5]
    array_02 = [9, 4, 9, 8, 4]
    assert solution(array_01, array_02) == [9, 4]
    print(solution(array_01, array_02))


