from collections import deque

DATA = [x.strip() for x in open("2021/inputs/day10.txt").readlines()]
PAIRS = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}
SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
OPENING = set(PAIRS.values())


def part_one() -> int:
    score = 0
    for line in DATA:
        stack = deque()
        for char in line:
            if char in OPENING:
                stack.append(char)
            elif stack[-1] == PAIRS[char]:
                stack.pop()
            else:
                score += SCORES[char]
                break
    return score


def part_two() -> int:
    return -1


print(part_one())
