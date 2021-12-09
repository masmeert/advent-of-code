from typing import List, Tuple

with open("2021/inputs/day09.txt") as f:
    DATA = [x.strip() for x in f.readlines()]
HEIGHT = len(DATA)
WIDTH = len(DATA[0])


def adjacent(i: int, j: int) -> Tuple[float | int]:
    return (
        float("inf") if i - 1 < 0 else int(DATA[i - 1][j]),
        float("inf") if i + 1 >= HEIGHT else int(DATA[i + 1][j]),
        float("inf") if j - 1 < 0 else int(DATA[i][j - 1]),
        float("inf") if j + 1 >= WIDTH else int(DATA[i][j + 1]),
    )


def get_lows() -> List[Tuple[int]]:
    lows = []
    for i in range(HEIGHT):
        for j in range(WIDTH):
            adj = adjacent(i, j)
            if int(DATA[i][j]) < min(adj):
                lows.append((i, j))
    return lows


def part_one() -> int:
    return sum(1 + int(DATA[low[0]][low[1]]) for low in get_lows())


def part_two() -> int:
    return -1


print(part_one())
print(part_two())
