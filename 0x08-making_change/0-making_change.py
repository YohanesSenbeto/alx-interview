#!/usr/bin/python3
"""
This module contains a function to determine the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The amount total to meet.

    Returns:
     If total cannot be met by any number of coins you have, return -1.
    """
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1

