def get_input():
    file = [line.split(",") for line in open("inputs/04.txt").read().split("\n")]
    for i in range(len(file)):
        for j in range(len(file[i])):
            file[i][j] = list(map(int, file[i][j].split("-")))

    return file


def part1(pairs):
    overlap = 0
    for pair in pairs:
        a, b = pair[0]
        c, d = pair[1]
        if (a <= c and d <= b) or (c <= a and b <= d):
            overlap += 1

    return overlap


def part2(pairs):
    overlap = 0
    for pair in pairs:
        a, b = pair[0]
        c, d = pair[1]
        if d >= a >= c or b >= c >= a:
            overlap += 1

    return overlap


if __name__ == "__main__":
    pairs = get_input()
    print(part1(pairs))
    print(part2(pairs))
