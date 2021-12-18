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
    check = lambda n, n2, a, a2: n2 - (n - n2) if a2 == a and n > n2 else n
    for instruction in INS:
        axis, line = instruction
        line = int(line)
        new_grid = set()
        for x, y in grid:
            new_grid.add((check(x, line, "x", axis), check(y, line, "y", axis)))
        if not p2:
            return new_grid
        grid = new_grid
    return grid


print(len(fold(False)))
grid = fold(True)
xmax, ymax = max(grid)
for y in range(ymax + 1):
    print("".join("█" if (x, y) in grid else "." for x in range(xmax + 1)))
