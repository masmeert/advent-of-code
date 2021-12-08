GROUPS = [group for group in open("2020/inputs/day06.txt").read().split("\n\n")]


def part_one() -> int:
    return sum(len(set(group.replace("\n", ""))) for group in GROUPS)


def part_two() -> int:
    return sum(
        sum(
            group.count(question) == len(group.split("\n"))
            for question in set(group.strip())
        )
        for group in GROUPS
    )


print(part_one())
print(part_two())
