"""
Pascal's Triangle

This problem was recently asked by AirBNB:

Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it.
Here's an example of the Pascal's Triangle of size 5.
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an integer n, generate the n-th row of the Pascal's Triangle.
"""

def pascal_triangle_row(n):
    row = [1] * n

    for i in range(n):
        last = row[0]
        for j in range(1, i):
            temp = row[j]
            row[j] = last + row[j]
            last = temp

    return row

if __name__ == "__main__":
    print(pascal_triangle_row(6))
    # [1, 5, 10, 10, 5, 1]