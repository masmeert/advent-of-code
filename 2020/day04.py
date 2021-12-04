with open("2020/inputs/day04") as f:
    DATA = [
        {sub[0]: sub[1] for sub in line if sub[0] != "cid"}
        for line in [
            [(x.split(":")) for x in x.split()] for x in f.read().split("\n\n")
        ]
    ]

def part_one():
    return sum(1 for x in DATA if len(x.keys()) == 7)

def part_two():
    checkers = {
            "byr": lambda x: 1920 <= int(x) <= 2002,
            "iyr": lambda x: 2010 <= int(x) <= 2020,
    }


print(part_one())
print(part_two())
