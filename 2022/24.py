DIRECTIONS = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}


def parse_input() -> list:
    with open("inputs/24.txt", "r") as f:
        data = f.read().strip().splitlines()[1:-1]

    grid = [list(line[1:-1]) for line in data]
    global N, M
    N = len(grid)
    M = len(grid[0])

    return [
        ((i, j), DIRECTIONS[char])
        for i, line in enumerate(grid)
        for j, char in enumerate(line)
        if char in DIRECTIONS
    ]


def travel(blizzards: list, start: tuple, end: tuple, step: int = 0) -> int:
    step += 1
    queue = set()
    while True:
        step += 1
        forbidden = {
            ((i + di * step) % N, (j + dj * step) % M) for (i, j), (di, dj) in blizzards
        }

        queue.add(start)
        next_queue = set()
        for i, j in queue:
            if (i, j) == end:
                return step
            for ni, nj in (i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if not 0 <= ni < N:
                    continue
                if not 0 <= nj < M:
                    continue
                if (ni, nj) in forbidden:
                    continue
                next_queue.add((ni, nj))
        queue = next_queue


if __name__ == "__main__":
    blizzards = parse_input()

    start, end = (0, 0), (N - 1, M - 1)

    first_travel = travel(blizzards, start, end)
    print(f"Part 1: {first_travel}")

    second_travel = travel(blizzards, end, start, first_travel)
    third_travel = travel(blizzards, start, end, second_travel)
    print(f"Part 2: {third_travel}")
