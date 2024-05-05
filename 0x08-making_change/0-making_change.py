#!/usr/bin/python3


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    If total is 0 or less, return 0
    If total cannot be met by any num of coins, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    memo = {0: 0}
    for amount in range(1, total + 1):
        memo[amount] = float("inf")
        for coin in coins:
            if amount - coin >= 0 and memo[amount - coin] != float("inf"):
                memo[amount] = min(memo[amount], memo[amount - coin] + 1)
    return memo[total] if memo[total] != float("inf") else -1
