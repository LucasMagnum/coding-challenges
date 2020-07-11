"""
Remove One Layer of Parenthesis

This problem was recently asked by Microsoft:

Given a valid parenthesis string (with only '(' and ')', an open parenthesis will always end with a close parenthesis,
and a close parenthesis will never start first), remove the outermost layers of the parenthesis string and return
the new parenthesis string.

If the string has multiple outer layer parenthesis (ie (())()), remove all outer layers and construct the new string.
So in the example, the string can be broken down into (()) + ().
By removing both components outer layer we are left with () + '' which is simply (), thus the answer for that input would be ().

Here are some examples and some starter code.

"""

def remove_outermost_parenthesis(s):
    result = ''
    parenthesis_level = 0

    for c in s:
        if c == '(':
            if parenthesis_level > 0:
                result += '('
            parenthesis_level += 1
        else:
            parenthesis_level -= 1
            if parenthesis_level > 0:
                result += ')'

    return result


if __name__ == "__main__":
    print(remove_outermost_parenthesis('(())()'))
    # ()

    print(remove_outermost_parenthesis('(()())'))
    # ()()

    print(remove_outermost_parenthesis('()()()'))
    # ' '
