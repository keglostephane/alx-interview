#!/usr/bin/python3
"""0-prime_game.py
"""


def isWinner(x, nums):
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
        return [p for p, prime in enumerate(is_prime) if prime]

    def play_game(n):
        primes = sieve(n)
        remaining = set(range(1, n + 1))
        turn = 0
        for prime in primes:
            if prime in remaining:
                remaining -= set(range(prime, n + 1, prime))
                turn = 1 - turn
        return turn

    maria_wins = sum(play_game(n) == 1 for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
