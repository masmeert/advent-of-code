from typing import List, Set

DATA = [x.strip() for x in open("2021/inputs/day09.txt").readlines()]
R, C = len(DATA), len(DATA[0])
DATA = {(k // C, k % C): int(DATA[k // C][k % C]) for k in range(R * C)}


def adjacents(coord: List[int]) -> Set[int]:
    r, c = coord
    return {
        DATA.get((r + 1, c), float("inf")),
        DATA.get((r - 1, c), float("inf")),
        DATA.get((r, c + 1), float("inf")),
        DATA.get((r, c - 1), float("inf")),
    }


def part_one() -> int:
    return sum(
        1 + height for coords, height in DATA.items() if height < min(adjacents(coords))
    )


def part_two() -> int:
    return -1


print(part_one())
