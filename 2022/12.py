from collections import defaultdict, deque


def adjacents(x: int, y: int):
    return set([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])


def get_height(char: str):
    return ord(char.replace("S", "a").replace("E", "z")) - 97


def find_path(grid: defaultdict, end: tuple):
    distances = defaultdict(lambda: float("inf"))
    distances[end] = 0
    queue = deque([end])
    p1, p2 = None, None

    while not p1 or not p2:
        current = queue.popleft()
        for adjacent in adjacents(*current):
            if get_height(grid[current]) - get_height(grid[adjacent]) <= 1:
                if distances[adjacent] == float("inf"):
                    queue.append(adjacent)
                distances[adjacent] = min(distances[adjacent], distances[current] + 1)

        if grid[current] == "S":
            p1 = distances[current]
        if grid[current] == "a" and not p2:
            p2 = distances[current]

    return p1, p2


if __name__ == "__main__":
    grid = defaultdict(lambda: "Z")
    for y, row in enumerate(open("inputs/12.txt").read().splitlines()):
        for x, char in enumerate(row):
            grid[(x, y)] = char
            if char == "E":
                end = (x, y)

    print(find_path(grid, end))
