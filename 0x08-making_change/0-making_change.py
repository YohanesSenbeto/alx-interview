#!/usr/bin/python3
"""
Making Change Problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of available coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet total, or -1 if no
             combination of coins can sum up to total.
    """
    if total <= 0:
        return 0

    coins = sorted(set(coins), reverse=True)
    min_coins = [float("inf")] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            a = min_coins[amount - coin] + 1
            min_coins[amount] = min(min_coins[amount], a)

    return min_coins[total] if min_coins[total] != float("inf") else -1
