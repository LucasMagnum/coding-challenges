"""
Nth Fibonacci Number

This problem was recently asked by Apple:

The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below are the first few values of the sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

Given a number n, print the n-th Fibonacci Number.
Examples:
Input: n = 3
Output: 2

Input: n = 7
Output: 13

"""
import math
import sys


def fib(nth):
    a, b = 0, 1 

    for _ in range(nth):
        a, b = a + b, a

    return a

def fib2(nth):
    if nth == 0:
        return 0
    if nth == 1:
        return 1
    
    return fib2(nth - 1) + fib2(nth - 2)


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        n = 11

    print(fib(n))
    print(fib2(40))
