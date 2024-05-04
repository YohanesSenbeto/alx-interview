#!/usr/bin/python3
"""
Making Change Problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    c = sorted(set(coins), reverse=True)
    dp = [0] + [float("inf")] * total

    """
    Iterate over each amount from 1 to total
    and each coin to find the minimum number of coins
    """
    for a in range(1, total + 1):
        for coin in c:
            if a >= coin:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
