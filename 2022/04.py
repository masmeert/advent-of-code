from utils import aoc

# type aliases
Bounds = tuple[int, int]
Pair = tuple[Bounds, Bounds]


def parse_range(range: str):
    start, end = map(int, range.split("-"))

    return start, end


def parse_input(input: list[str]) -> list[Pair]:
    pairs = []
    for line in input:
        ranges = line.split(",")
        pair = (parse_range(ranges[0]), parse_range(ranges[1]))
        pairs.append(pair)

    return pairs


def part_one(pairs: list[Pair]) -> int:
    overlaps = 0
    for pair in pairs:
        if (pair[0][0] <= pair[1][0] and pair[1][1] <= pair[0][1]) or (
            pair[1][0] <= pair[0][0] and pair[0][1] <= pair[1][1]
        ):
            overlaps += 1

    return overlaps


def part_two(pairs: list[Pair]) -> int:
    overlaps = 0
    for pair in pairs:
        if not (pair[0][1] < pair[1][0] or pair[1][1] < pair[0][0]):
            overlaps += 1

    return overlaps


if __name__ == "__main__":
    input = aoc.get_input("04")
    pairs = parse_input(input)
    print(part_one(pairs))
    print(part_two(pairs))
