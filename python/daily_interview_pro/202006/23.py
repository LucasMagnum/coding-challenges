"""
Determine if number

This problem was recently asked by Amazon:

Given a string that may represent a number, determine if it is a number.
Here's some of examples of how the number may be presented:

"123" # Integer
"12.3" # Floating point
"-123" # Negative numbers
"-.3" # Negative floating point
"1.5e5" # Scientific notation

Here's some examples of what isn't a proper number:
"12a" # No letters
"1 2" # No space between numbers
"1e1.2" # Exponent can only be an integer (positive or negative or 0)
Scientific notation requires the first number to be less than 10,
however to simplify the solution assume the first number can be greater than 10.
Do not parse the string with int() or any other python functions.
"""

from enum import Enum

class DigitState(Enum):
    BEGIN = 0
    NEGATIVE1 = 1
    DIGIT1 = 2
    DOT = 3
    DIGIT2 = 4
    E = 5
    NEGATIVE2 = 6
    DIGIT3 = 7

digit_lambdas = {
    DigitState.BEGIN: lambda x: True,
    DigitState.NEGATIVE1: lambda x: x == '-',
    DigitState.DIGIT1: lambda x: x.isdigit(),
    DigitState.DOT: lambda x: x == '.',
    DigitState.DIGIT2: lambda x: x.isdigit(),
    DigitState.E: lambda x: x == 'e',
    DigitState.NEGATIVE2: lambda x: x == '-',
    DigitState.DIGIT3: lambda x: x.isdigit()
}

fsm = {
    DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1],
    DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
    DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
    DigitState.DOT: [DigitState.DIGIT2],
    DigitState.DIGIT2: [DigitState.DIGIT2, DigitState.E],
    DigitState.E: [DigitState.DIGIT3, DigitState.NEGATIVE2],
    DigitState.NEGATIVE2: [DigitState.DIGIT3],
    DigitState.DIGIT3: [DigitState.DIGIT3]
}


def parse_number(s):
    state = DigitState.BEGIN

    for ch in s:
        found_next_state = False

        for next_state in fsm[state]:
            if digit_lambdas[next_state](ch):
                state = next_state
                found_next_state = True
                break

        if not found_next_state:
            return False

    return state in (DigitState.DIGIT1, DigitState.DIGIT2, DigitState.DIGIT3)


if __name__ == "__main__":
    print(parse_number("12.3"))
    # True

    print(parse_number("12a"))
    # False