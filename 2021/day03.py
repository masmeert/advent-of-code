from collections import Counter

with open("2021/inputs/day03") as f:
    DATA = [x.strip() for x in f.readlines()]
N = len(DATA[0])


def part_one():
    gamma = epsilon = ""
    for x in range(N):
        c = Counter(bits[x] for bits in DATA)
        gamma += c.most_common()[0][0]
        epsilon += c.most_common()[1][0]
    return int(gamma, 2) * int(epsilon, 2)


def part_two(o2, i=0, data=DATA):
    c = Counter(bits[i] for bits in data)
    common = c.most_common()
    if common[0][1] != common[1][1]:
        bit = common[0][0] if o2 else common[1][0]
    else:
        bit = "1" if o2 else "0"
    valid = [bits for bits in data if bits[i] == bit]
    if len(valid) == 1:
        return valid[0]
    return part_two(o2, i + 1, valid)


print(part_one())
print(int(part_two(True), 2) * int(part_two(False), 2))
