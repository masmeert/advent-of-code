import collections
import re
import math
from typing import Optional

Node = tuple[str, str]
Graph = dict[str, Node]


def read_input(filename: str) -> tuple[str, Graph]:
    node_maps = {}
    with open(filename, "r") as f:
        instructions, nodes = f.read().split("\n\n")
    for node in nodes.split("\n"):
        start, left, right = re.findall(r"\w+", node)
        node_maps[start] = (left, right)

    return instructions, node_maps


def part_one(instructions: str, node_maps: Graph, start: Optional[str] = "AAA") -> int:
    steps = 0
    instruction_count = -1
    position = start

    while position != "ZZZ":
        steps += 1
        instruction_count = (instruction_count + 1) % len(instructions)
        move = instructions[instruction_count]
        position = node_maps[position][0] if move == "L" else node_maps[position][1]

    return steps


def part_two(instructions: str, node_maps: Graph) -> int:
    steps_to_z = collections.defaultdict(list)
    seen = set()

    for position in node_maps:
        if position[-1] == "A":
            previous_position = position
            steps = 0
            instruction_count = -1

            while True:
                if position[-1] == "Z":
                    steps_to_z[previous_position].append(steps)

                steps += 1
                instruction_count = (instruction_count + 1) % len(instructions)
                move = instructions[instruction_count]

                current_state = (position, instruction_count)
                if current_state in seen:
                    break

                seen.add(current_state)
                position = (
                    node_maps[position][0] if move == "L" else node_maps[position][1]
                )

    all_steps = {
        int(x)
        for p, steps_list in steps_to_z.items()
        if p[-1] == "A"
        for x in steps_list
    }
    return math.lcm(*all_steps)


ins, nodes = read_input("inputs/08.txt")
print(part_one(ins, nodes))
print(part_two(ins, nodes))
