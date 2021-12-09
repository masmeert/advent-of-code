from typing import Dict, List, Tuple, Union
from collections import deque
from math import prod

DATA = [x.strip() for x in open("2021/inputs/day09.txt").readlines()]
R, C = len(DATA), len(DATA[0])
DATA = {(k // C, k % C): int(DATA[k // C][k % C]) for k in range(R * C)}


def adjacents(coord: List[int]) -> Dict[Tuple[int], Union[int, float]]:
    r, c = coord
    return {
        (r + 1, c): DATA.get((r + 1, c), float("inf")),
        (r - 1, c): DATA.get((r - 1, c), float("inf")),
        (r, c + 1): DATA.get((r, c + 1), float("inf")),
        (r, c - 1): DATA.get((r, c - 1), float("inf")),
    }


def part_one() -> int:
    return sum(
        1 + height
        for coords, height in DATA.items()
        if height < min(adjacents(coords).values())
    )


def part_two() -> int:
    sizes = []
    seen = set()
    for k in range(R * C):
        r, c = (k // C, k % C)
        if (r, c) not in seen and DATA.get((r, c)) != 9:
            size = 0
            stack = deque()
            stack.append((r, c))
            while stack:
                r, c = stack.popleft()
                if (r, c) in seen:
                    continue
                seen.add((r, c))
                size += 1
                for coords, height in adjacents((r, c)).items():
                    if height < 9:
                        stack.append(coords)
            sizes.append(size)
    return prod(sorted(sizes)[-3:])


print(part_one())
print(part_two())
