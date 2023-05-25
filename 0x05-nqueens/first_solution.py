#!/usr/bin/python3
"""The Module contains the solution to the
N-Queens Problem"""
import sys


class NQueenProblem:
    class Position:
        def __init__(self, row, col):
            self.row = row
            self.col = col

    def solveNQueenOneSolution(self, n):
        positions = [None] * n
        hasSolution = self.solveNQueenOneSolutionUtil(n, 0, positions)
        if hasSolution:
            return positions
        else:
            return []

    def solveNQueenOneSolutionUtil(self, n, row, positions):
        if n == row:
            return True
        for col in range(n):
            foundSafe = True
            for queen in range(row):
                if positions[queen].col == col or positions[queen].row \
                        - positions[queen].col == row - col or positions[
                    queen].row + positions[queen].col == row + col:
                    foundSafe = False
                    break
            if foundSafe:
                positions[row] = self.Position(row, col)
                if self.solveNQueenOneSolutionUtil(n, row + 1, positions):
                    return True
        return False

    def solveNQueens(self, n):
        result = []
        positions = [None] * n
        self.solve(0, positions, result, n)
        return result

    def solve(self, current, positions, result, n):
        if n == current:
            buff = ""
            oneResult = []
            for p in positions:
                for i in range(n):
                    if p.col == i:
                        buff += "Q"
                    else:
                        buff += "."
                oneResult.append(buff)
                buff = ""
            result.append(oneResult)
            return

        for i in range(n):
            foundSafe = True
            for j in range(current):
                if positions[j].col == i or positions[j].col - positions[j].row == i - current \
                        or positions[j].row + \
                        positions[j].col == i + current:
                    foundSafe = False
                    break
            if foundSafe:
                positions[current] = self.Position(current, i)
                self.solve(current + 1, positions, result, n)


s = NQueenProblem()
positions = s.solveNQueenOneSolution(int(sys.argv[1]))
for position in positions:
    print(position.row, position.col)
