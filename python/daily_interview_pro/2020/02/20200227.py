"""
Witness of The Tall People

This problem was recently asked by Google:

There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?

Example:
Input: [3, 6, 3, 4, 1]
Output: 3
Explanation: Only [6, 4, 1] were able to see in front of them.

  #
  #
  #   #
# # # #
# # # #
# # # # #
3 6 3 4 1                                 x (murder scene)

"""


def solution(line):
    count = 0
    highest = float("-inf")

    for height in line[::-1]:
        if height > highest:
            highest = height
            count += 1

    return count


if __name__ == "__main__":
    line = [3, 6, 3, 4, 1]
    print(f"Solution({line}) ->", solution(line))
