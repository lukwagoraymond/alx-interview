#!/usr/bin/python3
"""Function calculates perimeter of the island described in grid"""


def island_perimeter(grid):
    """
    Calculates perimeter of the island described in grid
    Args:
        grid: list of integers
    Returns:
        integer of perimeter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # cells with 2 sides side by side on top and bottom
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # cells with 2 sides side by side on left and right
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
