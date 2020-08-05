"""
Sum Binary Numbers

This problem was recently asked by Facebook:

Given two binary numbers represented as strings, return the sum of the two binary numbers
 as a new binary represented as a string.

Do this without converting the whole binary string into an integer.

"""

def sum_binary(bin1, bin2):
    backwards_idx = 1
    result = []
    carry = 0

    while backwards_idx <= len(bin1) or backwards_idx <= len(bin2):
        digit_sum = carry
        if backwards_idx <= len(bin1):
            digit_sum += ord(bin1[-backwards_idx]) - ord('0')

        if backwards_idx <= len(bin2):
            digit_sum += ord(bin2[-backwards_idx]) - ord('0')

        result.append(str(digit_sum % 2))
        carry = digit_sum // 2

        backwards_idx += 1

    if carry == 1:
        result.append('1')

    return ''.join(result[::-1])


if __name__ == "__main__":
    print(sum_binary("11101", "1011"))
    # 101000
