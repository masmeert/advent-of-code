from collections import defaultdict

ALGO = "".join(
    str(int(char == "#")) for char in open("2021/inputs/day20_1.txt").readline().strip()
)
IMG = [x.strip() for x in open("2021/inputs/day20_2.txt").readlines()]
IMG = defaultdict(
    lambda: "0",
    {(i, j): IMG[i][j] for j in range(len(IMG[0])) for i in range(len(IMG))},
)


def part_one() -> int:
    return -1


def part_two() -> int:
    return -1


print(part_one())
print(part_two())
