"""
Spreadsheet Columns

This problem was recently asked by Apple:

In many spreadsheet applications, the columns are marked with letters.
From the 1st to the 26th column the letters are A to Z.
Then starting from the 27th column it uses AA, AB, ..., ZZ, AAA, etc.

Given a number n, find the n-th column name.

def column_name(n):
  # Fill this in.

print column_name(26)
print column_name(27)
print column_name(28)
# Z
# AA
# AB


"""
import string

letters = list(string.ascii_uppercase)


def solution(number):
    if number <= len(letters):
        return letters[number - 1]

    return solution((number - 1) // len(letters)) + solution(number % len(letters))


if __name__ == "__main__":
    print(solution(26))
    print(solution(27))
    print(solution(28))