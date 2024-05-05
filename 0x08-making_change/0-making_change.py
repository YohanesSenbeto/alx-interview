#!/usr/bin/python3

"""Making Change Problem"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    If total is 0 or less, return 0
    If total cannot be met by any num of coins
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1
