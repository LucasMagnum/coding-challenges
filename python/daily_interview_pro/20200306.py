"""

Maximum Profit From Stocks

This problem was recently asked by Apple:

You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
"""


def brute_force(array):
    max_profit = 0
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            buy_price, sell_price = array[i], array[j]
            max_profit = max(max_profit, sell_price - buy_price)
    return max_profit


def solution(array):
    current_max, max_profit = 0, 0

    for index in range(len(array) - 1, -1, -1):
        price = array[index]
        current_max = max(current_max, price)
        potential_profit = current_max - price
        max_profit = max(max_profit, potential_profit)
    return max_profit


if __name__ == "__main__":
    array = [0, 9, 11, 8, 5, 7, 10, 2, 3, 7, 9]
    print(f"Solution({array})", brute_force(array))
    print(f"Solution({array})", solution(array))