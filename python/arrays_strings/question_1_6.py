"""
String Compression: 
    Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3, If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""
import sys
from typing import List, Tuple


def solution(string: str) -> str:
    compressed_data = _compress_string(string)

    original_string_size = len(string)
    compressed_string_size = len(compressed_data)

    if original_string_size <= compressed_string_size:
        return string

    return "".join(map(str, compressed_data))


def _compress_string(string: str) -> List[Tuple[str, int]]:
    counter = 0

    compressed = []
    string_size = len(string)

    for index, character in enumerate(string):
        counter += 1

        if index + 1 >= string_size or character != string[index + 1]:
            compressed.append(character)
            compressed.append(counter)
            counter = 0

    return compressed


if __name__ == "__main__":
    try:
        string = sys.argv[1]
    except IndexError:
        string = "aabcccccaaa"

    print(f"Solution :({string}) -> ", solution(string))
