#!/usr/bin/python3
"""
This module contains the minOperations function used to calculate
the minimum number of operations needed to result in exactly n H characters
in the file. It performs this by breaking down the target number into its
prime factors.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
