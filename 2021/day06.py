from typing import Dict

FISHES = {i: 0 for i in range(9)}
with open("2021/inputs/day06.txt") as f:
    for age in map(int, f.readline().split(",")):
        FISHES[age] += 1


def simulate_fishes(days: int, fishes: Dict[str, int] = FISHES) -> int:
    for _ in range(days):
        pregnant = fishes[0]
        for age in range(8):
            fishes[age] = fishes[age + 1]
        fishes[8] = pregnant
        fishes[6] += pregnant
    return sum(fishes.values())


# print(simulate_fishes(80))
print(simulate_fishes(256))
