from utils.math import gaussian_sum

DATA = sorted([int(x) for x in open("2021/inputs/day07.txt").readline().split(",")])


def part_one() -> int:
    return sum(abs(x - DATA[len(DATA) // 2]) for x in DATA)


def part_two() -> int:
    return min(sum(gaussian_sum(abs(n - x)) for n in DATA) for x in range(max(DATA)))


print(part_one())
print(part_two())
