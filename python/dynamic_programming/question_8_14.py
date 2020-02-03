"""
Boolean Evaluation:
    Given a boolean expression consisting of the symbols 0 (false), 1 (true), & (AND), | (OR), and ^ (XOR), and a desired boolean 
    result value `result`, implement a function to count the number of ways of parenthesizing the expression such that it evaluates
    to result.
    The expression should be fully parenthesized ( (0) ^ (1) ) but not extraneously ( ((0) ^ (1)) )

    Example:
        >> count_evaluation("1 ^ 0 | 0 | 1 ", false)
        2

        >> count_evaluation("0 & 0 & 0 & 1 ^ 1 | 0", true)
        10
"""


def count_evaluation(expression: str, result: bool, cache: dict) -> int:
    if len(expression) == 0:
        return 0

    if len(expression) == 1:
        evaluation = expression == "1"
        return 1 if evaluation is result else 0

    cache_key = (expression, result)
    if cache.get(cache_key) is not None:
        return cache[cache_key]

    ways = 0

    # For every second character
    for i in range(1, len(expression), 2):
        character = expression[i]

        left = expression[:i]
        right = expression[i + 1:]

        # Evaluate each side for each result 
        left_true = count_evaluation(left, True, cache)
        left_false = count_evaluation(left, False, cache)

        right_true = count_evaluation(right, True, cache)
        right_false = count_evaluation(right, False, cache)

        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        # XOR -> 1 True and 1 False
        if (character == "^"):
            total_true = (left_true * right_false) + (left_false * right_true)
        
        # AND -> both true
        elif (character == "&"):
            total_true = (left_true * right_true)
        
        # OR -> anything but both false
        elif (character == "|"):
            total_true = (
                (left_true * right_true) + 
                (left_false * right_true) + 
                (left_true * right_false)
            )

        sub_ways = total_true if result is True else total - total_true
        ways += sub_ways

    cache[cache_key] = ways
    return ways


if __name__ == "__main__":
    expression, result = "0&0&0&1^1|0", True
    print(f"Solution ({expression}): ", count_evaluation(expression, result, {}))