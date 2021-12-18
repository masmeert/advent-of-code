import sys
import os
import requests
from dotenv import load_dotenv

from utils.common import DIGITS


def format_day(day: str) -> str:
    return f"{int(day):02d}" if int(day) in DIGITS else day


def get_input(year: str, day: str):
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session}
    )
    if not res.ok:
        raise RuntimeError(
            f"Request failed, code: {res.status_code}, message: {res.content}"
        )
    return res.text[:-1]


def create_file(filename: str, content: str = "") -> None:
    try:
        f = open(filename, "x")
    except Exception as e:
        raise e
    else:
        f.write(content)
        f.close()
        print(f"Created {filename}")


if __name__ == "__main__":
    load_dotenv()
    session = os.getenv("session")
    year, day = sys.argv[1:]
    template = f"""DATA = [
    x.strip() for x in open("{year}/inputs/day{format_day(day)}.txt").readlines()
]


def part_one() -> int:
    return -1


def part_two() -> int:
    return -1


print(part_one())
print(part_two())
    """
    create_file(f"{year}/day{format_day(day)}.py", template)
    create_file(f"{year}/inputs/day{format_day(day)}.txt", get_input(year, day))
