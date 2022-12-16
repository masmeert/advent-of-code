if __name__ == "__main__":
    highest = sorted(
        list(
            map(
                lambda group: sum(map(int, group.split("\n"))),
                open("inputs/01.txt").read().split("\n\n"),
            )
        )
    )
    print("Part 1:", highest[-1])
    print("Part 2:", sum(highest[-3:]))
