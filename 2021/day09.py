from typing import Set, Tuple, Union
from utils import mul

with open("2021/inputs/day09.txt") as f:
    DATA = [x.strip() for x in f.readlines()]
HEIGHT = len(DATA)
WIDTH = len(DATA[0])


def adjacent(i: int, j: int) -> Tuple[Union[float, int]]:
    return (
        float("inf") if i - 1 < 0 else int(DATA[i - 1][j]),
        float("inf") if i + 1 >= HEIGHT else int(DATA[i + 1][j]),
        float("inf") if j - 1 < 0 else int(DATA[i][j - 1]),
        float("inf") if j + 1 >= WIDTH else int(DATA[i][j + 1]),
    )


def part_one() -> int:
    lows = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            adj = adjacent(i, j)
            if int(DATA[i][j]) < min(adj):
                lows += 1 + int(DATA[i][j])
    return lows


def part_two() -> int:
    pass


print(part_one())
print(part_two())
