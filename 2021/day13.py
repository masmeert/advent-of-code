DOTS = [
    [*map(int, x.strip().split(","))]
    for x in open("2021/inputs/day13_1.txt").readlines()
]
INSTRUCTIONS = [
    x.strip().replace("fold along ", "")
    for x in open("2021/inputs/day13_2.txt").readlines()
]
print(INSTRUCTIONS)


def part_one() -> int:
    return -1


def part_two() -> int:
    return -1


print(part_one())
print(part_two())
