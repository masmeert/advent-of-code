import math

with open("2021/day03/input.txt") as f:
    DATA = [x.strip() for x in f.readlines()]


def part_one():
    gamma = epsilon = ""
    for x in range(len(DATA[0])):
        counts = [0, 0]
        for bit in DATA:
            counts[int(bit[x])] += 1
        gamma += str(counts.index(max(counts)))
        epsilon += str(counts.index(min(counts)))
    return int(gamma, 2) * int(epsilon, 2)


def part_two():
    results = []
    for boolean in range(2):
        valid = DATA
        for i in range(len(DATA[0])):
            counts = [[], []]
            for bit in valid:
                counts[int(bit[i])].append(bit)
            if len(counts[1]) >= len(counts[0]):
                valid = counts[1 if boolean else 0]
            else:
                valid = counts[0 if boolean else 1]
            if len(valid) == 1:
                break
        results.append(valid[0])
    return math.prod(int(result, 2) for result in results)


print(part_one())
print(part_two())
