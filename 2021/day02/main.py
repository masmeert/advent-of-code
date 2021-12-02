from operator import mul

with open("2021/day02/input.txt") as f:
    DATA = [x.strip() for x in f.readlines()]


def part_one():
    return mul(
        sum(
            int(x[x.index(" ") + 1 :])
            if x[: x.index(" ")] == "down"
            else -int(x[x.index(" ") + 1 :])
            for x in DATA
            if x[: x.index(" ")] in ("up, down")
        ),
        sum(int(x[x.index(" ") + 1 :]) for x in DATA if x[: x.index(" ")] == "forward"),
    )


def part_two():
    aim = depth = horizontal = 0
    for x in DATA:
        x = x.split(" ")
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
