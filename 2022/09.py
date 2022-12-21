from utils import aoc

DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


def move(rope, direction):
    dx, dy = DIRECTIONS[direction]
    rope[0][0] += dx
    rope[0][1] += dy
    for i in range(1, len(rope)):
        if max(abs(rope[i - 1][0] - rope[i][0]), abs(rope[i - 1][1] - rope[i][1])) > 1:
            if rope[i - 1][0] != rope[i][0]:
                rope[i][0] += 1 if rope[i - 1][0] > rope[i][0] else -1
            if rope[i - 1][1] != rope[i][1]:
                rope[i][1] += 1 if rope[i - 1][1] > rope[i][1] else -1


def simulate(motions, rope_len):
    rope = [[0, 0] for _ in range(rope_len)]
    tail = set([tuple(rope[-1])])
    for direction, steps in motions:
        for _ in range(int(steps)):
            move(rope, direction)
            tail.add(tuple(rope[-1]))
    return len(tail)


if __name__ == "__main__":
    motions = list(map(str.split, aoc.get_input("09")))
    print(simulate(motions, 2))
    print(simulate(motions, 10))
