"""
Longest Common Prefix

This problem was recently asked by Microsoft:

Given a list of strings, find the longest common prefix between all strings.

"""


def longest_common_prefix(strs):
    prefix = []

    while len(prefix) < len(strs[0]):
        prefix_len = len(prefix)
        current_char = strs[0][prefix_len]

        for string in strs:
            if prefix_len >= len(string) or string[prefix_len] != current_char:
                return ''.join(prefix)

        prefix.append(current_char)
    return ''.join(prefix)


if __name__ == "__main__":
    print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
    # hell

    print(longest_common_prefix(['daily', 'interview', 'pro']))
    # ''