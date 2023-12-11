from itertools import combinations


Node = tuple[int, int]
Grid = list[Node]

_input = [line.strip() for line in open("inputs/11.txt", "r").readlines()]
GRID = [
    (x, y) for x, row in enumerate(_input) for y, cell in enumerate(row) if cell != "."
]
EMPTY_COLS = [i for i in range(len(_input[0])) if all(row[i] == "." for row in _input)]
EMPTY_ROWS = [i for i, row in enumerate(_input) if all(c == "." for c in row)]


def dist(galaxy: Node):
    return abs(galaxy[0][0] - galaxy[1][0]) + abs(galaxy[0][1] - galaxy[1][1])


def distances(universe: Grid):
    return [dist(galaxy) for galaxy in get_pairs(universe)]


def get_pairs(universe: Grid):
    return combinations(universe, 2)


def move(galaxy: Node, older=False):
    offset = 1 if not older else 999999
    return (
        galaxy[0] + sum(r < galaxy[0] for r in EMPTY_ROWS) * offset,
        galaxy[1] + sum(c < galaxy[1] for c in EMPTY_COLS) * offset,
    )


if __name__ == "__main__":
    expanded_universe = [move(galaxy) for galaxy in GRID]
    print(sum(distances(expanded_universe)))

    expanded_universe = [move(galaxy, True) for galaxy in GRID]
    print(sum(distances(expanded_universe)))
