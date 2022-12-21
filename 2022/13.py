import json
from utils import aoc
from math import prod
from functools import cmp_to_key as c


def compare(left, right):
    match left, right:
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case int(), int():
            return left - right
        case list(), list():
            for i, j in zip(left, right):
                if (r := compare(i, j)) != 0:
                    return r
            return compare(len(left), len(right))


if __name__ == "__main__":
    input = [json.loads(line) for line in aoc.get_input("13") if len(line)]

    p1 = sum(
        i + 1
        for i, (left, right) in enumerate(zip(input[::2], input[1::2]))
        if compare(left, right) <= 0
    )
    p2 = prod(
        i + 1
        for i, packet in enumerate(sorted(input + [[[2]], [[6]]], key=c(compare)))
        if packet in [[[2]], [[6]]]
    )
    print(p1, p2)
