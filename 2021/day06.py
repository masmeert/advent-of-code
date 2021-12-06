from collections import Counter


def simulate_fishes(days: int) -> int:
    fishes = Counter(
        int(x) for x in open("2021/inputs/day06.txt").read().strip().split(",")
    )
    for d in range(days):
        fishes[(d + 7) % 9] += fishes[d % 9]
    return sum(fishes.values())


print(simulate_fishes(80))
print(simulate_fishes(256))
