from functools import reduce
from itertools import product
import operator
import re

from utils import aoc


def parse_line(line) -> list[int]:
    return list(map(int, re.findall(r"\d+", line)))


def read_input() -> list[list[int]]:
    return list(map(parse_line, aoc.get_input("07")))


def concat(a: int, b: int) -> int:
    return int(f"{a}{b}")


def can_solve(operators, target: int, rest: list[int]) -> bool:
    return any(
        reduce(lambda acc, step: step[0](acc, step[1]), zip(comb, rest[1:]), rest[0])
        == target
        for comb in product(operators, repeat=len(rest) - 1)
    )


def get_calibration_result(operators, equations: list[list[int]]) -> int:
    return sum(
        target for target, *rest in equations if can_solve(operators, target, rest)
    )


if __name__ == "__main__":
    input = read_input()
    print(get_calibration_result([operator.add, operator.mul], input))
    print(get_calibration_result([operator.add, operator.mul, concat], input))
