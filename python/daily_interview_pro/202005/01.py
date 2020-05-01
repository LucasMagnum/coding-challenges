"""
Shifted String

This problem was recently asked by Apple:

You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

Eg. 
A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. 
A = abc and B= acb should return false.
"""

def solution(first, second):
    if len(first) != len(second):
        return False
    
    return second in first + first


if __name__ == "__main__":
    print(solution("abcde", "cdeab"))