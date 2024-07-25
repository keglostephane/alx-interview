#!/usr/bin/python3
"""makechange module
"""


def makeChange(coins, total):
    """Returns the minimum number of coins for a given amount.
    """
    if total <= 0:
        return 0

    # Handle edge case where no coins are provided
    if not coins:
        return -1

    # Initialize the dp array with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total of 0

    # Populate the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1
