from collections import Counter
from typing import List, Union

with open("2021/inputs/day03") as f:
    DATA = [x.strip() for x in f.readlines()]

N = len(DATA[0])


def part_one() -> int:
    gamma = epsilon = ""

    for i in range(N):
        c = Counter(bits[i] for bits in DATA)
        gamma += c.most_common()[0][0]
        epsilon += c.most_common()[1][0]

    return int(gamma, 2) * int(epsilon, 2)


def part_two(o2: bool, i: int = 0, data: List[str] = DATA) -> Union[List[str], int]:
    c = Counter(bits[i] for bits in data)
    common = c.most_common()
    bit = "1" if o2 else "0"

    if common[0][1] != common[1][1]:
        bit = common[0][0] if o2 else common[1][0]

    valid = [bits for bits in data if bits[i] == bit]

    if len(valid) == 1:
        return int(valid[0], 2)

    return part_two(o2, i + 1, valid)


print(part_one())
print(part_two(True) * part_two(False))
