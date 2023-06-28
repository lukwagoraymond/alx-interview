#!/usr/bin/python3
"""Prime number game"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None

    def sieve(n, tcase, i=2):
        if i > int(pow(n, 0.5)) + 1:
            tcase[0] = tcase[1] = False
            return
        if tcase[i]:
            for j in range(i * i, n + 1, i):
                tcase[j] = False
        sieve(n, tcase, i + 1)

    def countPrimes(tcase, i=0, c=0):
        if i == len(tcase):
            return
        if tcase[i]:
            c += 1
        tcase[i] = c
        countPrimes(tcase, i + 1, c)

    n = max(nums)
    tcase = [True for _ in range(max(n + 1, 2))]
    sieve(n, tcase)
    countPrimes(tcase)

    def calculateScore(nums, player1, i=0):
        if i == len(nums):
            if player1 * 2 == len(nums):
                return None
            if player1 * 2 > len(nums):
                return "Maria"
            return "Ben"
        player1 += tcase[nums[i]] % 2 == 1
        return calculateScore(nums, player1, i + 1)
    return calculateScore(nums, 0)
