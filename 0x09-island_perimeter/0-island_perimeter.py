#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ return the perimeter of the island described in grid """
    total_perimeter = 0

    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == 1:
                # Check edges
                if i == 0 or grid[i-1][j] == 0:
                    total_perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    total_perimeter += 1
                if j == 0 or row[j-1] == 0:
                    total_perimeter += 1
                if j == len(row) - 1 or row[j+1] == 0:
                    total_perimeter += 1

    return total_perimeter
