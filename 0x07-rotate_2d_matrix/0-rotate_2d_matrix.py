#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """
    Rotates an m by n 2D matrix in place.
    """
    if (
        not isinstance(matrix, list)
        or len(matrix) == 0
        or not all(isinstance(row, list) for row in matrix)
    ):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(len(row) == cols for row in matrix):
        return

    rotated_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - 1 - i] = matrix[i][j]

    matrix.clear()
    matrix.extend(rotated_matrix)
