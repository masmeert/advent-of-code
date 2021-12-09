import sys
import os
import requests
from dotenv import load_dotenv

load_dotenv()
SESSION = os.getenv("session")


def day_to_string(day: int) -> str | int:
    return f"{day:02d}" if day in {1, 2, 3, 4, 5, 6, 7, 8, 9} else day


def get_input(year: int, day: int):
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": SESSION}
    )
    if not res.ok:
        raise RuntimeError(
            f"Request failed, code: {res.status_code}, message: {res.content}"
        )
    return res.text[:-1]


def create_file(filename: str, content: str):
    try:
        f = open(filename, "x")
    except Exception as e:
        raise e
    else:
        f.write(content)


def main() -> None:
    year, day = sys.argv[1:]
    template = f"""with open("{year}/inputs/day{day_to_string(day)}.txt") as f:
    DATA = [x.strip() for x in f.readlines()]


def part_one() -> int:
    return -1


def part_two() -> int:
    return -1


print(part_one())
print(part_two())
    """
    create_file(f"{year}/day{day_to_string(day)}.py", template)
    create_file(f"{year}/inputs/day{day_to_string(day)}.txt", get_input(year, day))


if __name__ == "__main__":
    main()
