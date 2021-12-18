from collections import Counter

with open("2021/inputs/day05.txt") as f:
    LINES = [
        [tuple(map(int, coords.split(","))) for coords in line.strip().split(" -> ")]
        for line in f.readlines()
    ]  # [(x1, y1),(x2, y2)]


def count_points(part2: bool) -> int:
    points = Counter()
    delta = lambda x, y: 1 if x > y else -1
    for line in LINES:
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 == x2:
            points.update((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        elif y1 == y2:
            points.update((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
        elif part2 and abs(x2 - x1) == abs(y2 - y1):
            dx = delta(x2, x1)
            dy = delta(y2, y1)
            points.update((x1 + i * dx, y1 + i * dy) for i in range(abs(x2 - x1) + 1))
    return sum(count > 1 for count in points.values())


print(count_points(False))
print(count_points(True))
