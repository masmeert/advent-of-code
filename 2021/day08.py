"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....
  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

LENGTHS = {2: 1, 3: 7, 4: 4, 5: (2, 3, 5), 6: (0, 6, 9), 7: 8}
"""


with open("2021/inputs/day08.txt") as f:
    DATA = [[y.strip().split(" ") for y in x.strip().split("|")] for x in f.readlines()]


def part_one() -> int:
    return sum(sum(len(y) in {2, 4, 3, 7} for y in x[1]) for x in DATA)


def part_two() -> int:
    pass


print(part_one())
print(part_two())
