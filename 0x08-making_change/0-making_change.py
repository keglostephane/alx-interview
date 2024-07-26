#!/usr/bin/python3
"""makechange module
"""


def makeChange(coins, total):
    """Returns the minimum number of coins for a given amount.
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while (total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
