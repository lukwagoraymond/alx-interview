#!/usr/bin/python3
"""
    0-pascal_triangle.py: Determine Binomial Coefficients
    based on a number supplied to function
"""


def pascal_triangle(n):
    """
        returns a list of integers
        Args:
            n (int): number of lists
        Returns: binomial coefficients of given number
    """
    pas_triangle = list()

    if n <= 0:
        return pas_triangle
    for i in range(n):
        tmp_list = list()

        for j in range(i + 1):
            if j == 0 or j == i:
                tmp_list.append(1)
            else:
                tmp_list.append(pas_triangle[i - 1][j - 1]
                                + pas_triangle[i - 1][j])
        pas_triangle.append(tmp_list)
    return pas_triangle
