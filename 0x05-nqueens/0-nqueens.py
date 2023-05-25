#!/usr/bin/python3
"""The Module contains the solution to the
N-Queens Problem"""

import sys


def store_position(position, n):
    """Stores position of queen placement"""
    b = list()

    for i in range(n):
        for j in range(n):
            if j == position[i]:
                b.append([i, j])
    print(b)


def safe_position(position, queen, col, row):
    """Checks the rows, columns and diagonals to check if
    current queen position does not conflict with other
    queen positions"""
    return position[queen] in (col, col - queen + row, queen - row + col)


def solveNQueenOneSolutionUtil(position, row, n):
    """Recursive Function that finds a safe position where a queen
    can be positioned without attacking another queen"""
    if row == n:
        store_position(position, n)
    else:
        for col in range(n):
            foundSafe = True
            for queen in range(row):
                if safe_position(position, queen, col, row):
                    foundSafe = False
            if foundSafe:
                position[row] = col
                solveNQueenOneSolutionUtil(position, row + 1, n)


def build_chess_board(size):
    """Builds chase board based on size"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if n < 4:
    print('N must be at least 4')
    exit(1)

board_position = build_chess_board(int(n))
row = 0
solveNQueenOneSolutionUtil(board_position, row, int(n))
