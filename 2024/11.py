from functools import cache

from utils import aoc


@cache
def simulate(stone: int, blinks: int = 75) -> int:
    if blinks == 0:
        return 1
    if stone == 0:
        return simulate(1, blinks - 1)

    length = len(str(stone))

    if length % 2:
        return simulate(stone * 2024, blinks - 1)

    a = stone // 10 ** (length // 2)
    b = stone % 10 ** (length // 2)
    return simulate(a, blinks - 1) + simulate(b, blinks - 1)


if __name__ == "__main__":
    stones = list(map(int, aoc.get_input("11", " ")))
    print(stones)
    print(sum(map(simulate, stones)))
