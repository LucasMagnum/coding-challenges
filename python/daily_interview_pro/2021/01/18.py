"""
Maximum Profit From Stocks

This problem was recently asked by Apple:

You are given an array. Each element represents the price of a stock on that particular day.
Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5,
and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).

"""

def solution(stocks):
    smallest_stock, max_so_far = stocks[0], float("-inf")

    for stock in stocks:
        smallest_stock = min(smallest_stock, stock)
        profit = stock - smallest_stock

        max_so_far = max(max_so_far, profit)

    return max_so_far


if __name__ == "__main__":
    print(solution([9, 11, 8, 5, 7, 10]))