from collections import defaultdict
from itertools import combinations

from utils import aoc

Coords = tuple[int, int]
Grid = dict[Coords, str]
Frequency = set[Coords]

INPUT_SIZE = 50


def read_input() -> tuple[Grid, dict[str, Frequency]]:
    grid, frequencies = {}, defaultdict(set)
    lines = aoc.get_input("08")
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[(i, j)] = char
            if char != ".":
                frequencies[char].add((i, j))
    return grid, frequencies


def get_antinodes(grid: Grid, frequencies: dict[str, Frequency]) -> int:
    p1, p2 = set(), set()
    for antennas in frequencies.values():
        for a, b in combinations(antennas, 2):
            dx, dy = a[0] - b[0], a[1] - b[1]

            for dx_dir, dy_dir, origin in [(dx, dy, a), (-dx, -dy, b)]:
                next_cell = (origin[0] + dx_dir, origin[1] + dy_dir)
                if next_cell in grid:
                    p1.add(next_cell)

                for k in range(INPUT_SIZE):
                    extended_cell = (origin[0] + dx_dir * k, origin[1] + dy_dir * k)
                    if extended_cell in grid:
                        p2.add(extended_cell)
                    else:
                        break

    return len(p1), len(p2)


if __name__ == "__main__":
    grid, frequencies = read_input()
    print(get_antinodes(grid, frequencies))
