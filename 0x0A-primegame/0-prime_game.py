#!/usr/bin/python3
"""Prime number game"""


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    marias_wins = sum(len([num for num in primes[:n] if num]) % 2 == 1 for n in nums)
    bens_wins = x - marias_wins

    return 'Maria' if marias_wins < bens_wins else ('Ben' if marias_wins > bens_wins else None)
