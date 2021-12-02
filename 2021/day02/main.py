from operator import mul

with open("2021/day02/input.txt") as f:
    DATA = [x.strip().split(" ") for x in f.readlines()]


def part_one():
    return mul(
        sum(
            int(x[1]) if x[0] == "down" else -int(x[1])
            for x in DATA
            if x[0] in ("up, down")
        ),
        sum(int(x[1]) for x in DATA if x[0] == "forward"),
    )


def part_two():
    aim = depth = horizontal = 0
    for x in DATA:
        x[1] = int(x[1])
        if x[0] == "up":
            aim -= x[1]
        elif x[0] == "down":
            aim += x[1]
        else:
            horizontal += x[1]
            depth += x[1] * aim
    return depth * horizontal


print(part_one())
print(part_two())
