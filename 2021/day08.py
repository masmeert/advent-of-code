with open("2021/inputs/day08.txt") as f:
    DATA = [[y.strip().split(" ") for y in x.strip().split("|")] for x in f.readlines()]


def part_one() -> int:
    return sum(sum(len(y) in {2, 4, 3, 7} for y in x[1]) for x in DATA)


def part_two() -> int:
    pass


print(part_one())
print(part_two())
