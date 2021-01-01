"""
Majority Element

This problem was recently asked by AirBNB:

A majority element is an element that appears more than half the time.
Given a list with a majority element, find the majority element.

"""

def majority_element(nums):
    count = 0
    result = 0

    for num in nums:
        if count == 0:
            result = num

        if result == num:
            count += 1
        else:
            count -= 1

    return result

if __name__ == "__main__":
    print(majority_element([3, 5, 3, 3, 2, 4, 3]))
    # 3