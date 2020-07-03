"""
String to Integer

This problem was recently asked by LinkedIn:

Given a string, convert it to an integer without using the builtin str function.
You are allowed to use ord to convert a character to ASCII code.

Consider all possible cases of an integer.
In the case where the string is not a valid integer, return None.

"""


def convert_to_int(string):
    if not string:
        return None

    result = 0

    is_negative = string.startswith("-")
    string = string[1:] if is_negative else string

    ascii_zero = ord('0')

    for char in string:
        if not char.isdigit():
            return None
        result = result * 10 + ord(char) - ascii_zero

    return -result if is_negative else result


if __name__ == "__main__":
    print(convert_to_int('-105') + 1)
    # -104