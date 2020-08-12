"""
Generate Brackets

This problem was recently asked by Apple:

Given a number n, generate all possible combinations of n well-formed brackets.

"""

def generate_brackets(n):
    brackets_list = [set() for _ in range(n+1)]

    brackets_list[1].add("()")

    for i in range(2, n + 1):
        for s in brackets_list[i - 1]:
            brackets_list[i].add("(" + s + ")")

        for j in range(1, i):
            for s1 in brackets_list[j]:
                for s2 in brackets_list[i - j]:
                    brackets_list[i].add(s1 + s2)

    return list(brackets_list[-1])


if __name__ == "__main__":
    print(generate_brackets(1))
    # ['()']

    print(generate_brackets(3))
    # ['((()))', '(()())', '()(())', '()()()', '(())()']