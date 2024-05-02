#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given total amount.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total.

    Args:
        coins (list): List of coin values.
        total (int): Total amount to make change for.

    Returns:
        int: Fewest number of coins needed to meet total.
             Returns -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize array to store the minimum number of coins needed
    # for each total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
