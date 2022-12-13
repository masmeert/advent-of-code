DATA = [
    (move[0], int(value)) for move, value in map(str.split, open("2021/inputs/day02"))
]


def dive(part: int) -> int:
    fwd = depth = aim = 0

    for x in DATA:
        if x[0] == "f":
            fwd += x[1]
            depth += x[1] * aim
        else:
            aim += x[1] if x[0] == "d" else -x[1]

    return fwd * (aim if part == 1 else depth)


print(dive(1))
print(dive(2))
