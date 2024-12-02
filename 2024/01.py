from collections import Counter
from utils import aoc

def parse_input(input: list[str]) -> tuple[list[int], list[int]]:
   return map(sorted, zip(*[list(map(int, item.split())) for item in input]))


def find_distances(left: list[int], right: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))

def calculate_similarity(left: list[int], right: list[int]) -> int:
    rcount = Counter(right)
    return sum(x * rcount[x] for x in left)


if __name__ == "__main__":
    input = aoc.get_input("01")
    left, right = parse_input(input)
    print(find_distances(left, right))
    print(calculate_similarity(left, right))