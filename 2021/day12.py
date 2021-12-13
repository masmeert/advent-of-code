from collections import defaultdict, deque, Counter


data = [x.strip() for x in open("2021/inputs/day12.txt").readlines()]
GRAPH = defaultdict(set)
for line in data:
    a, b = line.split("-")
    GRAPH[a].add(b)
    GRAPH[b].add(a)


def count_paths(p2: bool) -> int:
    count = 0
    queue = deque([["start"]])
    while queue:
        path = queue.popleft()
        if path[-1] == "end":
            count += 1
            continue
        for c in GRAPH[path[-1]]:
            if (
                c.isupper()
                or c not in path
                or (
                    p2
                    and c not in ("start", "end")
                    and all(v <= 1 for k, v in Counter(path).items() if k.islower())
                )
            ):
                p = path.copy()
                p.append(c)
                queue.append(p)
    return count


print(count_paths(False))
print(count_paths(True))
