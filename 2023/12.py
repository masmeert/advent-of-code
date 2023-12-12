from functools import lru_cache


def read_input(filename: str) -> tuple[str, tuple[int]]:
    records = []
    with open(filename, "r") as f:
        input = f.read().splitlines()

    for line in input:
        parts = line.split(" ")
        spring, groups = parts[0], tuple(map(int, parts[1].split(",")))
        records.append((spring, groups))

    return records


@lru_cache
def find_arrangements(spring: str, groups: tuple[int]) -> int:
    if not spring:
        return 1 if not groups else 0

    if spring.startswith("."):
        return find_arrangements(spring.lstrip("."), groups)

    if spring.startswith("?"):
        return find_arrangements(
            spring.replace("?", ".", 1), groups
        ) + find_arrangements(spring.replace("?", "#", 1), groups)

    if spring.startswith("#"):
        if (
            not groups
            or len(spring) < groups[0]
            or any(c == "." for c in spring[: groups[0]])
        ):
            return 0

        if len(groups) > 1:
            if len(spring) < groups[0] + 1 or spring[groups[0]] == "#":
                return 0
            return find_arrangements(spring[groups[0] + 1 :], groups[1:])
        else:
            return find_arrangements(spring[groups[0] :], groups[1:])


def solve(springs: list[tuple[str, tuple[int]]], part2=False) -> int:
    arrangements = 0
    for spring, groups in springs:
        if part2:
            groups *= 5
            spring = "?".join([spring] * 5)
        arrangements += find_arrangements(spring, groups)
    return arrangements


if __name__ == "__main__":
    springs = read_input("inputs/12.txt")
    print(solve(springs))
    print(solve(springs, part2=True))
