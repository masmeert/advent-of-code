from itertools import count

SQUIDS = [line.strip() for line in open("2021/inputs/day11.txt").readlines()]
R, C = len(SQUIDS), len(SQUIDS[0])
SQUIDS = {(k // C, k % C): int(SQUIDS[k // C][k % C]) for k in range(R * C)}


def neighbors(row: int, col: int):
    return filter(
        SQUIDS.get,
        [
            (row + 1, col + 1),
            (row + 1, col),
            (row + 1, col - 1),
            (row, col + 1),
            (row - 1, col + 1),
            (row - 1, col - 1),
            (row - 1, col),
            (row, col - 1),
        ],
    )


flashed = 0
for i in count():
    if i == 100:
        print(f"p1: {flashed}")
    for c in SQUIDS:
        SQUIDS[c] += 1
    to_flash = {c for c in SQUIDS if SQUIDS[c] > 9}
    while to_flash:
        c = to_flash.pop()
        SQUIDS[c] = 0
        flashed += 1
        for a in neighbors(*c):
            SQUIDS[a] += 1
            if SQUIDS[a] > 9:
                to_flash.add(a)
    if sum(SQUIDS.values()) == 0:
        print(f"p2: {i+1}")
        break
