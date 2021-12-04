import sys

YEAR, DAY = sys.argv[1:]
TEMPLATE = f"""with open("{YEAR}/inputs/day{DAY}.txt") as f:
    DATA = [x.strip() for x in f.readlines()]


def part_one():
    return None


def part_two():
    return None


print(part_one())
print(part_two())
"""

try:
    f = open(f"{YEAR}/day{DAY}.py", "x")
except Exception as e:
    print(e)
else:
    f.write(TEMPLATE)
    f.close()