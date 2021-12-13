import matplotlib.pyplot as plt
from typing import Set, Tuple


DOTS = set(
    tuple(map(int, x.strip().split(",")))
    for x in open("2021/inputs/day13_1.txt").readlines()
)
INS = [
    x.strip().replace("fold along ", "").split("=")
    for x in open("2021/inputs/day13_2.txt").readlines()
]


def fold(p2: bool, grid: Set[Tuple[int]] = DOTS) -> Set[Tuple[int]]:
    for instruction in INS:
        axis, line = instruction
        line = int(line)
        new_grid = set()
        for x, y in grid:
            if axis == "x" and x > line:
                x = line - (x - line)
            elif axis == "y" and y > line:
                y = line - (y - line)
            new_grid.add((x, y))
        grid = new_grid
        if not p2:
            return grid
    return grid


print(len(fold(False)))
grid = fold(True)
xmax, ymax = max(grid)
for y in range(ymax + 1):
    print("".join("#" if (x, y) in grid else "." for x in range(xmax + 1)))
