from collections import Counter


def simulate_fishes(days: int) -> int:
    fishes = Counter(
        int(x) for x in open("2021/inputs/day06.txt").read().strip().split(",")
    )
    for _ in range(days):
        pregnant = fishes[0]
        for age in range(8):
            fishes[age] = fishes[age + 1]
        fishes[8] = pregnant
        fishes[6] += pregnant
    return sum(fishes.values())


print(simulate_fishes(80))
print(simulate_fishes(256))
