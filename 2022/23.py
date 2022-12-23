import functools
from utils import aoc
from collections import defaultdict


def parse_input() -> set[complex]:
    scan = aoc.get_input("23")
    return {
        x + 1j * y
        for y, line in enumerate(scan)
        for x, c in enumerate(line)
        if c == "#"
    }


def find_neighbors(elf: complex) -> list[complex]:
    return [
        elf - 1,
        elf + 1,
        elf - 1j,
        elf + 1j,
        elf + 1 + 1j,
        elf + 1 - 1j,
        elf - 1 + 1j,
        elf - 1 - 1j,
    ]


def find_moves(elf: complex) -> list:
    return [
        [[elf - 1j, elf + 1 - 1j, elf - 1 - 1j], elf - 1j],
        [[elf + 1j, elf + 1 + 1j, elf - 1 + 1j], elf + 1j],
        [[elf - 1 + 1j, elf - 1 - 1j, elf - 1], elf - 1],
        [[elf + 1 + 1j, elf + 1 - 1j, elf + 1], elf + 1],
    ]


def move(grid: set[complex], elf: complex, n_round: int) -> complex:
    elf_neighbors = find_neighbors(elf)
    elf_moves = find_moves(elf)

    if all(not neighbor in grid for neighbor in elf_neighbors):
        return elf

    for i in range(n_round, n_round + 4):
        if all(move not in grid for move in elf_moves[i % len(elf_moves)][0]):
            return elf_moves[i % len(elf_moves)][1]

    return elf


def play(grid: set[complex], n_round: int) -> tuple[set[complex], bool]:
    moved = False
    moves = defaultdict(list)
    new_grid = set()

    for elf in grid:
        new_elf = move(grid, elf, n_round)
        if new_elf != elf:
            moved = True
        moves[new_elf].append(elf)

    for k, v in moves.items():
        if len(v) == 1:
            new_grid.add(k)
        else:
            new_grid.update(v)

    return new_grid, moved


def part1() -> float:
    grid = parse_input()
    for round_n in range(10):
        grid, _ = play(grid, round_n)
    imaginaries = sorted([i.imag for i in grid])
    reals = sorted([i.real for i in grid])
    return (reals[-1] - reals[0] + 1) * (1 + imaginaries[-1] - imaginaries[0]) - len(
        grid
    )


@functools.cache
def part2() -> int:
    moved = True
    grid = parse_input()
    round_n = 0

    while moved:
        grid, moved = play(grid, round_n)
        round_n += 1

    return round_n


if __name__ == "__main__":
    print(part1())
    print(part2())
