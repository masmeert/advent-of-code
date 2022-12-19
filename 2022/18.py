DIRECTIONS = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))


def get_input():
    global mini, maxi, pairs
    mini, maxi, pairs = 1, 10, 0
    cubes = set()
    with open("inputs/18.txt", "r") as f:
        for line in f.readlines():
            coords = tuple(map(int, line.split(",")))
            for k in coords:
                mini = min(mini, k)
                maxi = max(maxi, k)
            cubes.add(coords)
            for delta in DIRECTIONS:
                if tuple(map(sum, zip(coords, delta))) in cubes:
                    pairs += 1
        return cubes

 
def get_nb_sides(coords):
    nb_sides = []
    for delta in DIRECTIONS:
        nb = tuple(map(sum, zip(coords, delta)))
        for k in nb:
            if not (mini - 1 <= k <= maxi + 1):
                break
        else:
            nb_sides.append(nb)
    return nb_sides
 
def dfs(cubes, start):
    q = [start]
    closed = {start}
    while q:
        current = q.pop()
        for nbr in get_nb_sides(current):
            if nbr in closed:
                continue
            if nbr in cubes:
                continue
            q.append(nbr)
            closed.add(nbr)
    return closed

def part2(cubes):
    steam_cells = dfs(cubes, (mini - 1, mini - 1, mini - 1))
    result = 0
    for cube in cubes:
        for nbr in get_nb_sides(cube):
            if nbr in steam_cells:
                result += 1
    return result

if __name__ == "__main__":
    cubes = get_input()
    print(6 * len(cubes) - 2 * pairs)
    print(part2(cubes))