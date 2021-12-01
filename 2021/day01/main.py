with open("2021/day01/input.txt") as f:
    DATA = [int(x) for x in f.readlines()]


def part_one():
    return sum(DATA[x] > DATA[x - 1] for x in range(1, len(DATA)))


def part_two():
    return sum(DATA[x] > DATA[x - 3] for x in range(3, len(DATA)))


print(part_one())
print(part_two())
