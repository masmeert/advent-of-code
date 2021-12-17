with open("2020/inputs/day02") as f:
    DATA = [
        {
            "bounds": tuple(int(a) for a in line[0].split("-")),
            "letter": line[1][0],
            "password": line[2],
        }
        for line in [line.strip().split(" ") for line in f.readlines()]
    ]


def part_one() -> int:
    return sum(
        x["bounds"][0] <= x["password"].count(x["letter"]) <= x["bounds"][1]
        for x in DATA
    )


def part_two() -> int:
    return sum(
        (x["password"][x["bounds"][0] - 1] == x["letter"])
        ^ (x["password"][x["bounds"][1] - 1] == x["letter"])
        for x in DATA
    )


print(part_one())
print(part_two())
