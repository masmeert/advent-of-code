import re
import math
from collections import deque


def get_input():
    with open("inputs/19.txt", "r") as f:
        file = f.read().splitlines()

    blueprints = []
    for line in file:
        values = tuple(map(int, re.findall(r"\d+", line)))
        blueprints.append(
            {
                "id": values[0],
                "ore": values[1],
                "clay": values[2],
                "obsidian": (values[3], values[4]),
                "geode": (values[5], values[6]),
            }
        )

    return blueprints


def solve(blueprint, time):
    queue = deque()
    seen = set()

    queue.append((0, (0, 0, 0, 0, 1, 0, 0, 0)))
    max_opened = 0

    while len(queue) > 0:
        time_left, other = queue.popleft()
        max_opened = max(max_opened, other[3])

        if time_left == time or other in seen:
            continue

        seen.add(other)

        if (
            other[3]
            + other[-1] * (time - time_left)
            + (time - time_left) * (time - time_left + 1) // 2
        ) <= max_opened:
            continue
        if (
            other[0] >= blueprint["ore"]
            and other[4]
            < max(
                blueprint["ore"],
                blueprint["clay"],
                blueprint["obsidian"][0],
                blueprint["geode"][0],
            )
            and other[0] + (time - time_left) * other[4]
            < (time - time_left)
            * max(
                blueprint["ore"],
                blueprint["clay"],
                blueprint["obsidian"][0],
                blueprint["geode"][0],
            )
        ):
            queue.append(
                (
                    time_left + 1,
                    (
                        other[0] - blueprint["ore"] + other[4],
                        other[1] + other[5],
                        other[2] + other[6],
                        other[3] + other[-1],
                        other[4] + 1,
                        other[5],
                        other[6],
                        other[-1],
                    ),
                )
            )
        if (
            other[0] >= blueprint["clay"]
            and other[5] < blueprint["obsidian"][1]
            and other[1] + (time - time_left) * other[5]
            < (time - time_left) * blueprint["obsidian"][1]
        ):
            queue.append(
                (
                    time_left + 1,
                    (
                        other[0] - blueprint["clay"] + other[4],
                        other[1] + other[5],
                        other[2] + other[6],
                        other[3] + other[-1],
                        other[4],
                        other[5] + 1,
                        other[6],
                        other[-1],
                    ),
                )
            )
        if (
            other[0] >= blueprint["obsidian"][0]
            and other[1] >= blueprint["obsidian"][1]
            and other[6] < blueprint["geode"][1]
            and other[2] + (time - time_left) * other[6]
            < (time - time_left) * blueprint["geode"][1]
        ):
            queue.append(
                (
                    time_left + 1,
                    (
                        other[0] - blueprint["obsidian"][0] + other[4],
                        other[1] - blueprint["obsidian"][1] + other[5],
                        other[2] + other[6],
                        other[3] + other[-1],
                        other[4],
                        other[5],
                        other[6] + 1,
                        other[-1],
                    ),
                )
            )
        if other[0] >= blueprint["geode"][0] and other[2] >= blueprint["geode"][1]:
            queue.append(
                (
                    time_left + 1,
                    (
                        other[0] - blueprint["geode"][0] + other[4],
                        other[1] + other[5],
                        other[2] - blueprint["geode"][1] + other[6],
                        other[3] + other[-1],
                        other[4],
                        other[5],
                        other[6],
                        other[-1] + 1,
                    ),
                )
            )
        else:
            queue.append(
                (
                    time_left + 1,
                    (
                        other[0] + other[4],
                        other[1] + other[5],
                        other[2] + other[6],
                        other[3] + other[-1],
                        other[4],
                        other[5],
                        other[6],
                        other[-1],
                    ),
                )
            )

    return max_opened


if __name__ == "__main__":
    blueprints = get_input()

    print(sum(blueprint["id"] * solve(blueprint, 24) for blueprint in blueprints))
    print(math.prod(solve(blueprints[i], 32) for i in range(3)))
