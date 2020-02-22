"""
Robot in a Grid:
    Imagine a robot sitting on the upper left corner of a grid with R rows and C columns.
    The robot can only move in two directions, right and down, 
    but certain cells are "off-limits" such that the robot cannot step on them. 
    Design an algorithm to find a path for the robot from the top left to the
    bottom right.
"""
import sys
from collections import namedtuple
from typing import List, Set

Point = namedtuple("Point", ("row", "column"))


def solution(grid: List[List[bool]]):
    path = []
    failed = set()

    if get_path(grid, len(grid) - 1, len(grid[0]) - 1, path, failed):
        return path

    return


def get_path(
    grid: List[List[bool]], row: int, col: int, path: List[Point], failed: Set[Point]
):
    if col < 0 or row < 0 or not grid[row][col]:
        return False

    point = Point(row, col)
    is_at_origin = row == 0 and col == 0

    # If we already computed this value, just ignore it
    if point in failed:
        return False

    # If there's a path from start to here add it to the path
    if (
        is_at_origin
        or get_path(grid, row, col - 1, path, failed)
        or get_path(grid, row - 1, col, path, failed)
    ):
        path.append(point)
        return True

    failed.add(point)
    return False


if __name__ == "__main__":
    # False means it's blocked, True means it's free
    grid = [
        [True, False, True, True, True],
        [True, True, False, True, True],
        [True, False, True, True, True],
        [True, True, True, True, True],
    ]

    grid_2 = [
        [True, True, True, True, True],
        [True, False, True, True, True],
        [True, False, True, False, False],
        [True, False, True, True, True],
    ]

    print("Result Grid 01: ", solution(grid))
    print("Result Grid 02: ", solution(grid_2))
