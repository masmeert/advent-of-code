SQUIDS = [line.strip() for line in open("2021/inputs/day11.txt").readlines()]
R, C = len(SQUIDS), len(SQUIDS[0])
SQUIDS = {(k // C, k % C): int(SQUIDS[k // C][k % C]) for k in range(R * C)}


def adjacents(r: int, c: int):
    return filter(
        SQUIDS.get,
        [
            (r + 1, c + 1),
            (r + 1, c),
            (r + 1, c - 1),
            (r, c + 1),
            (r - 1, c + 1),
            (r - 1, c - 1),
            (r - 1, c),
            (r, c - 1),
        ],
    )


def part_one() -> int:
    total = 0
    for _ in range(100):
        for c in SQUIDS:
            SQUIDS[c] += 1
        to_flash = {c for c in SQUIDS if SQUIDS[c] > 9}
        while to_flash:
            c = to_flash.pop()
            SQUIDS[c] = 0
            total += 1
            for a in adjacents(*c):
                SQUIDS[a] += 1
                if SQUIDS[a] > 9:
                    to_flash.add(a)
    return total


def part_two() -> int:
    return -1


print(part_one())
print(part_two())
