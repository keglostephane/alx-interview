#!/usr/bin/python3
"""0-prime_game.py
"""


def isWinner(x, nums):
    """Determines the winner of prime game"""
    if not nums or x < 1:
        return None

    max_num = max(nums)

    is_prime = [True] * (max(max_num + 1, 2))
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    prime_count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_count += 1
        is_prime[i] = prime_count

    maria_wins = 0
    for n in nums:
        if is_prime[n] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == len(nums):
        return None
    elif maria_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
