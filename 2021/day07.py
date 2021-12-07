from utils import gaussian_sum

with open("2021/inputs/day07.txt") as f:
    DATA = sorted([int(x) for x in f.readline().split(",")])


def part_one() -> int:
    return sum(abs(x - DATA[len(DATA) // 2]) for x in DATA)


def part_two() -> int:
    return sum(gaussian_sum(abs(x - sum(DATA) // len(DATA))) for x in DATA)


print(part_one())
print(part_two())
