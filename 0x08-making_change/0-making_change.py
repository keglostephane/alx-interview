#!/usr/bin/python3
"""makechange module
"""


def makeChange(coins, total):
    """Returns the minimum number of coins for a given amount.
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    # Initialize a list to store the minimum number of coins needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
