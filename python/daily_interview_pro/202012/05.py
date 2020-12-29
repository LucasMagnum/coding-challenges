"""
Fix Brackets

This problem was recently asked by Twitter:

Given a string with only ( and ),
find the minimum number of characters to add or
 subtract to fix the string such that the brackets are balanced.

Example:
Input: '(()()'
Output: 1
Explanation:

The fixed string could either be ()() by deleting the first bracket,
or (()()) by adding a bracket.
These are not the only ways of fixing the string,
there are many other ways by adding it in different positions!

"""

def fix_brackets(string):
    fix_count = 0
    bracket_count = 0

    for char in string:
        if char == "(":
            bracket_count += 1
        elif char == ")":
            if bracket_count == 0:
                fix_count += 1
            else:
                bracket_count -= 1
    return fix_count + bracket_count

if __name__ == "__main__":
    print(fix_brackets('(()()'))
    # 1