from utils import aoc

Coords = tuple[int, int]
Grid = dict[Coords, str]


def read_input() -> Grid:
    lines = aoc.get_input("04")
    return {
        (y, x): char
        for y, row in enumerate(lines)
        for x, char in enumerate(row.strip())
    }


def get_grid_dimensions(grid: Grid) -> Coords:
    max_y = max(y for y, _ in grid)
    max_x = max(x for _, x in grid)
    return max_y + 1, max_x + 1


def get_word_at_position(
    grid: Grid, start: Coords, direction: Coords, length: int
) -> str:
    (y, x) = start
    (dy, dx) = direction
    result = []
    for i in range(length):
        curr = (y + i * dy, x + i * dx)
        if curr not in grid:
            return ""
        result.append(grid[curr])
    return "".join(result)


def part_one(grid: Grid) -> int:
    height, width = get_grid_dimensions(grid)
    target = "XMAS"
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    return sum(
        get_word_at_position(grid, (y, x), d, len(target)) == target
        for y in range(height)
        for x in range(width)
        for d in directions
    )


def part_two(grid: Grid) -> int:
    height, width = get_grid_dimensions(grid)

    def is_mas(s: str) -> bool:
        return s in ["MAS", "SAM"]

    count = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            down_right = get_word_at_position(grid, (y - 1, x - 1), (1, 1), 3)
            down_left = get_word_at_position(grid, (y - 1, x + 1), (1, -1), 3)
            if down_right and down_left:
                if (is_mas(down_right) or is_mas(down_right[::-1])) and (
                    is_mas(down_left) or is_mas(down_left[::-1])
                ):
                    count += 1
    return count


if __name__ == "__main__":
    grid = read_input()
    print(part_one(grid))
    print(part_two(grid))
