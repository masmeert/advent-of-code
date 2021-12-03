from utils import mul
from collections import Counter

with open("2021/inputs/day03") as f:
    DATA = [x.strip() for x in f.readlines()]
N = len(DATA[0])


def part_one():
    gamma = epsilon = ""
    for x in range(N):
        c = Counter()
        for bits in DATA:
            c[bits[x]] += 1
        gamma += c.most_common()[0][0]
        epsilon += c.most_common()[1][0]
    return int(gamma, 2) * int(epsilon, 2) 


def part_two():
    results = []
    for bit in range(2):
        valid = DATA
        for i in range(N):
            counts = [[], []]
            for bits in valid:
                counts[int(bits[i])].append(bits)
            if len(counts[1]) >= len(counts[0]):
                valid = counts[1 if bit else 0]
            else:
                valid = counts[0 if bit else 1]
            if len(valid) == 1:
                break
        results.append(valid[0])
    return mul(int(result, 2) for result in results)


print(part_one())
print(part_two())
