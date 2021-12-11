from collections import deque

DATA = [x.strip() for x in open("2021/inputs/day10.txt").readlines()]
PAIRS = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}
OPENING = set(PAIRS.values())


def part_one() -> int:
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in DATA:
        stack = deque()
        for char in line:
            if char in OPENING:
                stack.append(char)
            elif stack[-1] == PAIRS[char]:
                stack.pop()
            else:
                score += scores[char]
                break
    return score


def part_two() -> int:
    return -1


print(part_one())
