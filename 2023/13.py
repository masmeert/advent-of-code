def read_input() -> list[list[str]]:
    with open("inputs/13.txt", "r") as f:
        grids = f.read().split("\n\n")
    return [[row for row in grid.split("\n")] for grid in grids]


def solve(grid: list[str], p2=False) -> int:
    helper = lambda g: sum(
        i + 1
        for i in range(len(g) - 1)
        if sum(sum(x != y for x, y in zip(a, b)) for a, b in zip(g[i + 1 :], g[i::-1]))
        == p2
    )
    return helper(grid) * 100 + helper([*zip(*grid)])


if __name__ == "__main__":
    grids = read_input()
    print(sum(map(solve, grids)))
    print(sum([solve(grid, p2=True) for grid in grids]))
