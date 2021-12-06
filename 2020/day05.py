import re

with open("2020/inputs/day05.txt") as f:
    DATA = set(
        (
            int(re.sub("[FL]", "0", re.sub("[BR]", "1", line)), 2)
            for line in f.read().split("\n")
        )
    )


def part_one():
    return max(DATA)


def part_two():
    return re.sub("[{}]", "", str(set(range(min(DATA), max(DATA))) - DATA))


print(part_one())
print(part_two())
