from ..utils.advent import prod

with open("2020/inputs/day03") as f:
    DATA = [x.strip() for x in f.readlines()]
N = len(DATA[0])


def count_trees(fwd: int, height: int) -> int:
    x = y = trees = 0

    while y < len(DATA):
        if DATA[y][x % N] == "#":
            trees += 1
        x += fwd
        y += height

    return trees


print(count_trees(3, 1))
print(
    prod(
        [
            count_trees(1, 1),
            count_trees(3, 1),
            count_trees(5, 1),
            count_trees(7, 1),
            count_trees(1, 2),
        ]
    )
)
