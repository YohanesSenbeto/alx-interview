#!/usr/bin/python3
"""
N Queens Problem.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens_util(board, col, n, res):
    """
    A recursive utility function to solve N Queens problem
    """
    if col == n:
        res.append([col[:] for col in board])
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            solve_nqueens_util(board, col + 1, n, res)

            board[i][col] = 0

    return False


def solve_nqueens(n):
    """
    Solves the N queens problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    res = []
    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0, n, res)
    sorted_res = sorted(res, key=lambda x: x[0].index(1))
    for solution in sorted_res:
        print(
            "[{}]".format(
                ", ".join(
                    ["[{}, {}]".format(i, solution[i].index(1)) for i in range(n)]
                )
            )
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
