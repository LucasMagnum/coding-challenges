"""
This problem was recently asked by Microsoft:

Given a string, determine if there is a way to arrange the string such that the string is a palindrome.
If such arrangement exists, return a palindrome (There could be many arrangements). Otherwise return None.

"""

def solution(string):
    counter = {}

    for char in string:
        counter[char] = counter.get(char, 0) + 1

    palindrome = ""
    odd_char = ""

    for char, count in counter.items():
        if count % 2 == 0:
            palindrome += char * (count // 2)
        elif not odd_char:
            odd_char = char
            palindrome += char * (count // 2)
        else:
            return None

    return palindrome + odd_char + palindrome[::-1]


if __name__ == "__main__":
    print(solution("mommo"))
    print(solution("aan"))
    print(solution("lucas"))