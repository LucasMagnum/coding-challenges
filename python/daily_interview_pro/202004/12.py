"""
Decode String

This problem was recently asked by Google:

Given a string with a certain rule: k[string] should be expanded to string k times.
So for example, 3[abc] should be expanded to abcabcabc.
Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

"""

def solution(string):
    result = ""
    i = 0

    while i < len(string):
        if string[i].isalpha():
            result += string[i]
            i += 1
            continue

        if string[i].isdigit():
            number = 0
            while string[i].isdigit():
                number = number * 10 + int(string[i])
                i += 1

        bracket = 1
        i += 1

        inner_string = ""
        while bracket > 0:
            if string[i] == "[": bracket += 1
            if string[i] == "]": bracket -= 1

            inner_string += string[i]
            i += 1

        result = result + number * solution(inner_string[:-1])
    return result


if __name__ == "__main__":
    print(solution("2[a2[b]c]"))