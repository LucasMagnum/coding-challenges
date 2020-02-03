"""
English Int:
   Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four") 
"""
import random
import sys


mapping = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eigtheen",
    19: "Nineteen",
    20: "Tweenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1_000: "Thousand",
    1_000_000: "Million",
    1_000_000_000: "Billion",
}


def print_number(number: int):
    key_by_largest = sorted(mapping.keys(), reverse=True)

    if number == 0:
        return

    for key in key_by_largest:
        number_by_key = number // key

        if number_by_key > 1:
            print_number(number_by_key)

        if number_by_key != 0:
            if number > 100 and number_by_key == 1:
                print(mapping[number_by_key], end=" ")
            print(mapping[key], end=" ")
            number = number % key


if __name__ == "__main__":
    try:
        number = int(sys.argv[1])
    except IndexError:
        number = random.randint(0, 100_000)

    print(f"Printing {number}")
    print_number(number)