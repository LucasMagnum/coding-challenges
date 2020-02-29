"""
Falling Dominoes

This problem was recently asked by Twitter:

Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

Example:
    Input:  ..R...L..R.
    Output: ..RR.LL..RR

The time complexity of this solution is O(n), since only a 2 pass is done.
The space complexity is O(n) as extra space is used to store the state of the dominos that fell over.

"""


def solution(string: str) -> str:
    size = len(string)
    forces = [0 for _ in range(size)]
    force = 0

    for i in range(size):
        if string[i] == "R":
            force = size
        elif string[i] == "L":
            force = 0
        else:
            force = max(force - 1, 0)

        forces[i] += force

    force = 0
    for i in range(size - 1, -1, -1):
        if string[i] == "L":
            force = size
        elif string[i] == "R":
            force = 0
        else:
            force = max(force - 1, 0)

        forces[i] -= force

    new_string = list(string)
    for index, force in enumerate(forces):
        if force == 0:
            new_string[index] = "."
        elif force > 0:
            new_string[index] = "R"
        else:
            new_string[index] = "L"

    return "".join(new_string)


if __name__ == "__main__":
    string = "..R...L..R."
    print(f"Solution({string}) -> ", solution(string))