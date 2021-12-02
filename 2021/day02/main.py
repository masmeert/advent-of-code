from operator import mul

with open("2021/day02/input.txt") as f:
    DATA = [(move, int(value)) for move, value in map(str.split, f)]


def part_one():
    return mul(
        sum(x[1] if x[0] == "down" else -x[1] for x in DATA if x[0] in ("up, down")),
        sum(x[1] for x in DATA if x[0] == "forward"),
    )


def part_two():
    aim = depth = horizontal = 0
    for x in DATA:
        if x[0] == "forward":
            horizontal += x[1]
            depth += x[1] * aim
        else:
            aim += -x[1] if x[0] == "up" else x[1]
    return depth * horizontal


print(part_one())
print(part_two())
