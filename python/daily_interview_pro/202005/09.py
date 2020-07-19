"""
Absolute Path

This problem was recently asked by Facebook:

Given a file path with folder names, '..' (Parent directory), and '.' (Current directory), 
return the shortest possible file path (Eliminate all the '..' and '.').

Example
Input: '/Users/Joma/Documents/../Desktop/./../'
Output: '/Users/Joma/'

"""


def solution(path):
    stack = []

    for folder in path.split("/"):
        if folder == "..":
            stack.pop()

        elif folder != ".":
            stack.append(folder)

    return "/".join(stack)


if __name__ == "__main__":
    print(solution("/Users/Joma/Documents/../Desktop/./../"))
