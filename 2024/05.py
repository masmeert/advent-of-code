from typing import Iterable
from collections import defaultdict, deque

from utils import aoc


def read_input() -> tuple[list[tuple[int, int]], list[list[int]]]:
    return [
        [list(map(int, line.split(d))) for line in part.split("\n")]
        for part, d in zip(aoc.get_input("05", "\n\n"), ["|", ","])
    ]


def is_valid(update: list[int], rules: list[tuple[int, int]]) -> bool:
    return all(
        update.index(a) < update.index(b)
        for a, b in rules
        if a in update and b in update
    )


def reorder_update(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    adj = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        if x in update and y in update:
            adj[x].append(y)
            in_degree[y] += 1
    queue = deque(p for p in update if in_degree[p] == 0)
    ordered = []
    while queue:
        page = queue.popleft()
        ordered.append(page)
        for neighbor in adj[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return ordered


def middle_page_sum(updates: Iterable[list[int]]) -> int:
    return sum(u[len(u) // 2] for u in updates)


def part_one(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    return middle_page_sum(u for u in updates if is_valid(u, rules))


def part_two(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    return middle_page_sum(
        reorder_update(u, rules) for u in updates if not is_valid(u, rules)
    )


if __name__ == "__main__":
    rules, updates = read_input()
    print(part_one(rules, updates))
    print(part_two(rules, updates))
