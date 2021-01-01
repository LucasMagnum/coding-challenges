"""
Remove Adjacent Duplicate Characters

This problem was recently asked by Apple:

Given a string, we want to remove 2 adjacent characters that are the same,
and repeat the process with the new string until we can no longer perform the operation.

"""

def remove_adjacent_dup(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)


if __name__ == "__main__":
    print(remove_adjacent_dup("cabba"))
    # Start with cabba
    # After remove bb: caa
    # After remove aa: c
    # print c