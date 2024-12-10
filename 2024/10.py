from collections import deque

from utils import aoc

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def read_input():
    return [[int(c) for c in line] for line in aoc.get_input("10")]


def explore_trails(tmap, count_paths=False):
    total = 0
    starts = [
        (i, j) for i, row in enumerate(tmap) for j, val in enumerate(row) if val == 0
    ]
    for start in starts:
        q = deque([(start, [])] if count_paths else [start])
        visited, scores, paths = set(), set(), 0
        while q:
            pos, trail = q.popleft() if count_paths else (q.popleft(), None)
            if pos in visited and not count_paths:
                continue
            visited.add(pos)
            x, y = pos
            if tmap[x][y] == 9:
                paths += count_paths
                scores.add(pos)
                continue
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(tmap)
                    and 0 <= ny < len(tmap[0])
                    and tmap[nx][ny] == tmap[x][y] + 1
                ):
                    q.append(
                        ((nx, ny), trail + [(nx, ny)]) if count_paths else (nx, ny)
                    )
        total += paths if count_paths else len(scores)
    return total


if __name__ == "__main__":
    tmap = read_input()
    print(explore_trails(tmap))
    print(explore_trails(tmap, count_paths=True))
