#!/usr/bin/python3
"""Module contains solutions to the 2D Matrix problem"""


def rotate_2d_matrix(matrix):
    """Rotates nxn Matrix in 90 degrees
    clockwise"""
    n = len(matrix[0])
    # Transpose Matrix
    for row in range(n):
        for col in range(row, n):
            matrix[col][row], \
                matrix[row][col] = matrix[row][col], \
                matrix[col][row]

    # Reverse Array in each row
    for row in range(n):
        arr = matrix[row]
        matrix[row] = arr[::-1]
