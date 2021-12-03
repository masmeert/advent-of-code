from operator import mul

with open("2021/day02/input") as f:
    DATA = [(move[0], int(value)) for move, value in map(str.split, f)]


def part_one():
    return mul(
        sum(x[1] if x[0] == "d" else -x[1] for x in DATA if x[0] in "ud"),
        sum(x[1] for x in DATA if x[0] == "f"),
    )


def part_two():
    aim = depth = horizontal = 0
    for x in DATA:
        if x[0] == "f":
            horizontal += x[1]
            depth += x[1] * aim
        else:
            aim += -x[1] if x[0] == "u" else x[1]
    return depth * horizontal


print(part_one())
print(part_two())
