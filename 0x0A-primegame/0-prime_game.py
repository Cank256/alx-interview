#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of each game of Prime Game.
    Arguments:
    x -- the number of rounds
    nums -- array of n for each round
    Returns:
    name of the player that won the most rounds
    """

    if not nums or x < 1:
        return None

    # Create a sieve of Eratosthenes to find all primes up to the max n in nums
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for start in range(2, int(max_n ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False

    # Prepare prime counts for every number up to max_n
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
