"""

Look and Say Sequence

This problem was recently asked by Google:

A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.

"""


def solution(nth):
    result = "1"

    for i in range(1, nth):
        new_result = ""

        previous_character = result[0]
        count = 0

        for character in result:
            if character == previous_character:
                count += 1
                continue

            new_result += str(count) + previous_character
            count = 1
            previous_character = character

        result = new_result + str(count) + previous_character

    return result


if __name__ == "__main__":
    print(solution(10))
