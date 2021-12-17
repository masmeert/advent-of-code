import heapq

DATA = [[int(x) for x in line.strip()] for line in open("2021/inputs/day15.txt")]


def solve(target, part2: bool):
    grid = {}
    for y in range(len(DATA)):
        for x in range(len(DATA[y])):
            grid[(x, y)] = DATA[y][x]
    R = C = len(DATA[0])
    distances = {
        (x, y): float("inf") for x in range(len(DATA[0])) for y in range(len(DATA))
    }
    distances[(0, 0)] = 0
    if part2:
        grid_copy = grid.copy()
        for i in range(5):
            for j in range(5):
                if i + j == 0:
                    continue
                shift_x = R * i
                shift_y = C * j
                for (x, y), val in grid_copy.items():
                    new_x = x + shift_x
                    new_y = y + shift_y
                    val += i + j
                    while val > 9:
                        val -= 9
                    grid[(new_x, new_y)] = val
                    distances[(new_x, new_y)] = float("inf")
        R *= 5
        C *= 5
    q = []
    heapq.heappush(q, (0, (0, 0)))
    visited = set()
    _, current = heapq.heappop(q)
    adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while True:
        for x, y in adjacents:
            dx = current[0] + x
            dy = current[1] + y
            if dx in range(R) and dy in range(C):
                distance = distances[current] + grid[(dx, dy)]
                if distance < distances[(dx, dy)]:
                    distances[(dx, dy)] = distance
                    heapq.heappush(q, (distance, (dx, dy)))
        visited |= {current}
        if target in visited:
            return distances
        _, current = heapq.heappop(q)


target = (len(DATA) - 1, len(DATA) - 1)
print(solve(target, False)[target])
target = (5 * (len(DATA)) - 1, 5 * (len(DATA)) - 1)
print(solve(target, True)[target])
