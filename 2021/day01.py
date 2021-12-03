with open("2021/inputs/day01") as f:
    DATA = [int(x) for x in f.readlines()]


def increases(step: int) -> int:
    return sum(DATA[i] > DATA[i - step] for i in range(step, len(DATA)))


print(increases(1))
print(increases(3))
