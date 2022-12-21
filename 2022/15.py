import re
from utils import aoc


def parse_input():
    disc = []

    file = aoc.get_input("15")

    sensors = {}
    for line in file:
        x, y, beacon_x, beacon_y = list(map(int, re.findall("-?\d+", line)))
        radius = abs(beacon_x - x) + abs(beacon_y - y)
        disc.append((x, y, radius))
        sensors[(x, y)] = (beacon_x, beacon_y)

    return sensors, disc


def part1(sensors):
    empty_tiles = set()
    row = 2000000

    for item in sensors.items():
        sensor, beacon = item
        radius = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

        steps = radius - abs(row - sensor[1])
        if steps < 0:
            continue

        for x in range(sensor[0] - steps, sensor[0] + steps + 1):
            pos = (x, row)
            if pos != (beacon[0], beacon[1]):
                empty_tiles.add(pos)

    return len(empty_tiles)


def get_boundary(x, y, radius):
    temp = (x, y + radius)
    while temp != (x + radius, y):
        temp = (temp[0] + 1, temp[1] - 1)
        yield temp
    while temp != (x, y - radius):
        temp = (temp[0] - 1, temp[1] - 1)
        yield temp
    while temp != (x - radius, y):
        temp = (temp[0] - 1, temp[1] + 1)
        yield temp
    while temp != (x, y + radius):
        temp = (temp[0] + 1, temp[1] + 1)
        yield temp


def part2(disc):
    freq = []
    for x, y, r in disc:
        for px, py in get_boundary(x, y, r + 1):
            if not (0 <= px <= 4000000 and 0 <= py <= 4000000):
                continue
            for dx, dy, dr in disc:
                if (abs(px - dx) + abs(py - dy)) <= dr:
                    break
            else:
                freq.append(4000000 * px + py)
    return freq[-1]


if __name__ == "__main__":
    sensors, disc = parse_input()
    print(part1(sensors))
    print(part2(disc))
