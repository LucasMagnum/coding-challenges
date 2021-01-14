"""
Multiply

Given two strings which represent non-negative integers, multiply the two numbers and
return the product as a string as well. You should assume that the numbers may be sufficiently
large such that the built-in integer type will not be able to store
the input (Python does have BigNum, but assume it does not exist).

"""

def multiply(str1, str2):
    result = []
    for power, digit in enumerate(str2[::-1]):
        add_num(result, multiply_digit(str1, digit), power)

    return "".join(map(str, result[::-1]))


def multiply_digit(str1, mult_digit):
    if str1 == "0" or mult_digit == "0":
        return [0]

    mult_digit = ord(mult_digit) - ord("0")
    result = []

    carry = 0

    for digit in str1[::-1]:
        digit_product = (ord(digit) - ord("0")) * mult_digit
        result.append(digit_product % 10 + carry)

        carry = digit_product // 10

    if carry > 0:
        result.append(carry)
    return result


def add_num(result, num, power):
    carry = 0
    i = 0

    while i < len(num):
        if i + power >= len(result):
            result.append(0)

        result[i + power] += num[i] + carry
        if result[i + power] > 9:
            carry = 1
            result[i + power] -= 10
        else:
            carry = 0

        i += 1


if __name__ == "__main__":
    print(multiply("11", "13"))
    # 143