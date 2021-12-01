with open("2021/day01/input.txt") as f:
    DATA = [int(x) for x in f.readlines()]


def part_one(data=DATA):
    return sum(data[x] > data[x - 1] for x in range(1, len(data)))


def part_two():
    return part_one(
        [DATA[x] + DATA[x - 1] + DATA[x - 2] for x in range(2, len(DATA))]
    )


print(part_one())
print(part_two())
