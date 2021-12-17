import re

with open("2020/inputs/day04.txt") as f:
    DATA = [
        {sub[0]: sub[1] for sub in line if sub[0] != "cid"}
        for line in [
            [(x.split(":")) for x in x.split()] for x in f.read().split("\n\n")
        ]
    ]


def part_one():
    return sum(len(x.keys()) == 7 for x in DATA)


def part_two():

    return sum(
        all(
            {
                "byr": lambda x: 1920 <= int(x) <= 2002,
                "iyr": lambda x: 2010 <= int(x) <= 2020,
                "eyr": lambda x: 2020 <= int(x) <= 2030,
                "hgt": lambda x: 150 <= int(x[:-2]) <= 193
                if x[-2:] == "cm"
                else 59 <= int(x[:-2]) <= 76
                if x[-2:] == "in"
                else False,
                "hcl": lambda x: re.search("^#(\d|[a-f]){6}$", x),
                "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
                "pid": lambda x: re.search("^\d{9}$", x),
            }[k](v)
            for k, v in x.items()
        )
        for x in DATA
        if len(x.keys()) == 7
    )


print(part_one())
print(part_two())
