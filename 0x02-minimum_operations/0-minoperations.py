#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file"""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    num_operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            num_operations += min_operations
            n /= min_operations
        min_operations += 1
    return num_operations
