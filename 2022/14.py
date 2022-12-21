from utils import aoc


def parse_input():
    cave = {}

    for line in aoc.get_input("14"):
        coords = line.split(" -> ")
        for f, t in zip(coords[0::], coords[1::]):
            (fx, fy) = (int(n) for n in f.split(","))
            (tx, ty) = (int(n) for n in t.split(","))

            for x in range(min(fx, tx), max(fx, tx) + 1):
                cave[x, fy] = "#"

            for y in range(min(fy, ty), max(fy, ty) + 1):
                cave[fx, y] = "#"

    return cave


def bottom(cave):
    return max(y for (_, y), val in cave.items() if val == "#")


def drop_sand(cave):
    x = 500

    for y in range(max(y for (_, y), val in cave.items() if val == "#")):
        if (x, y + 1) not in cave:
            pass
        elif (x - 1, y + 1) not in cave:
            x -= 1
        elif (x + 1, y + 1) not in cave:
            x += 1
        else:
            cave[(x, y)] = "o"
            return (x, y) != (500, 0)

    return False


def add_floor(cave):
    bottom_y = bottom(cave)
    for x in range(-1000, 1000):
        cave[x, bottom_y + 2] = "#"


def simulate(bottom_is_abyss):
    cave = parse_input()

    if not bottom_is_abyss:
        add_floor(cave)

    while drop_sand(cave):
        pass

    return cave


if __name__ == "__main__":
    p1 = sum(1 for v in simulate(True).values() if v == "o")
    p2 = sum(1 for v in simulate(False).values() if v == "o")
    print(p1, p2)
