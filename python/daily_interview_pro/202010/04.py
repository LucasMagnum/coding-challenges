"""
Longest common prefix

Given a list of strings, find the longest common prefix between all strings.
"""


def longest_common_prefix(strings):
    prefix = []

    while len(prefix) < len(strings[0]):
        prefix_len = len(prefix)
        current_char = strings[0][prefix_len]

        for string in strings:
            if prefix_len >= len(string) or string[prefix_len] != current_char:
                return "".join(prefix)

        prefix.append(current_char)

    return "".join(prefix)


if __name__ == "__main__":
    print(longest_common_prefix(["helloworld", "hellokitty", "hell"]))
    # hell

    print(longest_common_prefix(["daily", "interview", "pro"]))
    # ''
