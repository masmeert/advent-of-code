import re


def parse_memory() -> list[str]:
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    with open("inputs/03.txt", "r") as f:
        memory = f.read()
    return re.findall(pattern, memory)


def part_one(instructions: list[str]) -> int:
    return sum(int(x) * int(y) for token, x, y in instructions if "mul" in token)


def part_two(instructions: list[str]) -> int:
    enabled = True
    total = 0
    for token, x, y in instructions:
        if "do()" in token:
            enabled = True
        elif "don't()" in token:
            enabled = False
        elif "mul" in token and enabled:
            total += int(x) * int(y)
    return total


if __name__ == "__main__":
    instructions = parse_memory()
    print(part_one(instructions))
    print(part_two(instructions))
