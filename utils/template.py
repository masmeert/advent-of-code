import sys
import os
import requests
from dotenv import load_dotenv

load_dotenv()
SESSION = os.getenv("session")
YEAR, DAY = sys.argv[1:]
TEMPLATE = f"""with open("{YEAR}/inputs/day{DAY}.txt") as f:
    DATA = [x.strip() for x in f.readlines()]


def part_one() -> int:
    return -1


def part_two() -> int:
    return -1


print(part_one())
print(part_two())
"""


def day_to_string() -> str:
    if len(str(DAY)) == 1:
        return "0" + str(DAY)
    return DAY


def get_input():
    res = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{DAY}/input", cookies={"session": SESSION}
    )
    if not res.ok:
        raise RuntimeError(
            f"Request failed, code: {res.status_code}, message: {res.content}"
        )
    return res.text[:-1]


# code template
try:
    f = open(f"{YEAR}/day{day_to_string()}.py", "x")
except Exception as e:
    print(e)
else:
    f.write(TEMPLATE)
    f.close()

# input
try:
    data = get_input()
    f = open(f"{YEAR}/inputs/day{day_to_string()}.txt", "x")
except Exception as e:
    print(e)
else:
    f.write(data)
    f.close()
