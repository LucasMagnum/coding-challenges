"""
Add Digits

This problem was recently asked by Amazon:

Given a number like 159, add the digits repeatedly until you get a single number.

For instance, 1 + 5 + 9 = 15.
1 + 5 = 6.

So the answer is 6.

"""


def solution(number):
    total = 0

    while number:
        total = total + number % 10
        number = number // 10

    return total


if __name__ == "__main__":
    print(solution(15951))
    # 1 + 5 + 9 + 5 + 1 = 21