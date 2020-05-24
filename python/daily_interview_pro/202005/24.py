"""
This problem was recently asked by Facebook:

Kaprekar's Constant is the number 6174.
This number is special because it has the property where for any 4-digit number that has 2
or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.

This certain function is as follows:
- Order the number in ascending form and descending form to create 2 numbers.
- Pad the descending number with zeros until it is 4 digits in length.
- Subtract the ascending number from the descending number.
- Repeat.

Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant.

print num_kaprekar_iterations(123)
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
"""

KAPREKAR_CONSTANT = 6174


def num_kaprekar_iterations(n):
    if n == KAPREKAR_CONSTANT:
        return 0

    n_str = str(n)
    asc_num = int("".join(sorted(n_str)))
    desc_str = sorted(n_str, reverse=True)

    desc_str = desc_str + ["0"] * (4 - len(desc_str))
    desc_num = int("".join(desc_str))

    new_num = desc_num - asc_num
    return num_kaprekar_iterations(new_num) + 1


if __name__ == "__main__":
    print(num_kaprekar_iterations(432))