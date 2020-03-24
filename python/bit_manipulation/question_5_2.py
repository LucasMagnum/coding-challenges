"""
Binary to String

Given a real number between 0 and 1 (e.g 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary
with at most 32 characters, print "ERROR".
"""


def solution(number):
    if number >= 1 or number <= 0:
        return "ERROR"

    binary = []
    binary.append(".")

    frac = 0.5

    while number > 0:
        if len(binary) > 64:
            return "ERROR"

        if number >= frac:
            binary.append(1)
            number -= frac
        else:
            binary.append(0)

        frac /= 2

    return "".join(map(str, binary))


if __name__ == "__main__":
    print(solution(0.101))
