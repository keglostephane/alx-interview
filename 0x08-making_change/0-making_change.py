#!/usr/bin/python3
"""makechange module
"""


def makeChange(coins, total):
    """Returns the minimum number of coins for a given amount.
    """
    if not total:
        return 0

    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != total + 1 else -1
