from typing import Dict

FISHES = {i: 0 for i in range(9)}
with open("2021/inputs/day06.txt") as f:
    for line in f:
        for age in map(int, line.split(",")):
            FISHES[age] += 1


def simulate_fishes(days: int, fishes: Dict[str, int] = FISHES) -> int:
    for _ in range(days):
        t = fishes[0]
        for j in range(0, 8):
            fishes[j] = fishes[j + 1]
        fishes[8] = t
        fishes[6] += t
    return sum(fishes.values())


# print(simulate_fishes(80))
print(simulate_fishes(256))
