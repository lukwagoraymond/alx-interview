#!/usr/bin/python3
"""Module containing solution to the making change question"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    current_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = divmod((total-current_total), coin)
        current_total += r[0] * coin
        coin_used += r[0]
        if current_total == total:
            return coin_used
    return -1
