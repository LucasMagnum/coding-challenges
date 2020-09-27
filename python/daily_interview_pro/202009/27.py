"""
Add Digits

This problem was recently asked by Amazon:

Given a number like 159, add the digits repeatedly until you get a single number.

For instance, 1 + 5 + 9 = 15.
1 + 5 = 6.

So the answer is 6.

"""

def solution(number):
    result = number

    while result >= 10:
        total = 0

        while result:
            total += result % 10
            result = result // 10

        result = total

    return result


if __name__ == "__main__":
    print(solution(159))
    # 1 + 5 + 9 = 15
    # 1 + 5 = 6
    # 6
