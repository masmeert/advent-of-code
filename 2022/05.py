import re
from utils import aoc


def get_input():
    instructions = aoc.get_input("05")
    for i in range(len(instructions)):
        regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
        instructions[i] = list(map(int, regex.search(instructions[i]).groups()))

    stacks = [
        ["Q", "F", "M", "R", "L", "W", "C", "V"],
        ["D", "Q", "L"],
        ["P", "S", "R", "G", "W", "C", "N", "B"],
        ["L", "C", "D", "H", "B", "Q", "G"],
        ["V", "G", "L", "F", "Z", "S"],
        ["D", "G", "N", "P"],
        ["D", "Z", "P", "V", "F", "C", "W"],
        ["C", "P", "D", "M", "S"],
        ["Z", "N", "W", "T", "V", "M", "P", "C"],
    ]

    return instructions, stacks


def get_top(stacks):
    top = ""
    for stack in stacks:
        top += stack[-1]

    return top


def move(instructions, stacks):
    for instruction in instructions:
        move, from_stack, to_stack = instruction
        for _ in range(move):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())


def move2(instructions, stacks):
    for instruction in instructions:
        move, from_stack, to_stack = instruction
        remove = stacks[from_stack - 1][-move:]
        del stacks[from_stack - 1][-move:]
        stacks[to_stack - 1].extend(remove)


def part1():
    instructions, stacks = get_input()
    move(instructions, stacks)
    return get_top(stacks)


def part2():
    instructions, stacks = get_input()
    move2(instructions, stacks)
    return get_top(stacks)


if __name__ == "__main__":
    print(part1())
    print(part2())
