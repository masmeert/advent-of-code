from utils import aoc, arrays


def sum_snacks_calories(snacks: list[str]) -> int:
    calories = arrays.parseInts(snacks.split("\n"))
    return sum(calories)


def rank_elves_by_calories(elves_snacks: list[str]) -> list[int]:
    elves_calories = []
    for snacks in elves_snacks:
        calories = sum_snacks_calories(snacks)
        elves_calories.append(calories)

    return sorted(elves_calories)


if __name__ == "__main__":
    elves = aoc.get_input("01", "\n\n")
    highest = rank_elves_by_calories(elves)
    print("Part 1:", highest[-1])
    print("Part 2:", sum(highest[-3:]))
