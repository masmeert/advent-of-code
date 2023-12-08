import re
import math


def read_input(filename):
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file]


def find_adj(board):
    ajd = {
        (r, c): []
        for r in range(len(board))
        for c in range(len(board[0]))
        if board[r][c] not in "01234566789."
    }

    for r, row in enumerate(board):
        row_str = "".join(row)
        for match in re.finditer(r"\d+", row_str):
            edge = {
                (r, c)
                for r in (r - 1, r, r + 1)
                for c in range(match.start() - 1, match.end() + 1)
            }

            for coord in edge & ajd.keys():
                ajd[coord].append(int(match.group()))

    return ajd


if __name__ == "__main__":
    board = read_input("inputs/03.txt")
    chars = find_adj(board)

    print(sum(sum(p) for p in chars.values()))
    print(sum(math.prod(p) for p in chars.values() if len(p) == 2))
