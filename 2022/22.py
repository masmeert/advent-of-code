BOARD, PATH = open("inputs/22.txt").read().split("\n\n")
BOARD = BOARD.split("\n")
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
REGIONS = [(0, 1), (0, 2), (1, 1), (2, 1), (2, 0), (3, 0)]
ROWS = len(BOARD)
COLS = len(BOARD[0])
CUBE = COLS // 3
for r in range(ROWS):
    while len(BOARD[r]) < COLS:
        BOARD[r] += " "


def region_to_global(r, c, region):
    rr, cc = REGIONS[region - 1]
    return (rr * CUBE + r, cc * CUBE + c)


def get_region(r, c):
    for i, (rr, cc) in enumerate(REGIONS):
        if rr * CUBE <= r < (rr + 1) * CUBE and cc * CUBE <= c < (cc + 1) * CUBE:
            return (i + 1, r - rr * CUBE, c - cc * CUBE)


def new_coords(r, c, d, nd):
    if d == 0:
        x = c
    if d == 1:
        x = r
    if d == 2:
        x = CUBE - 1 - c
    if d == 3:
        x = CUBE - 1 - r

    if nd == 0:
        return (CUBE - 1, x)
    if nd == 1:
        return (x, 0)
    if nd == 2:
        return (0, CUBE - 1 - x)
    if nd == 3:
        return (CUBE - 1 - x, CUBE - 1)


def get_dest(r, c, d, part):
    if part == 1:
        r = (r + DIRECTIONS[d][0]) % ROWS
        c = (c + DIRECTIONS[d][1]) % COLS
        while BOARD[r][c] == " ":
            r = (r + DIRECTIONS[d][0]) % ROWS
            c = (c + DIRECTIONS[d][1]) % COLS
        return (r, c, d)

    region, rr, rc = get_region(r, c)
    newRegion, nd = {
        (4, 0): (3, 0),
        (4, 1): (2, 3),
        (4, 2): (6, 3),
        (4, 3): (5, 3),
        (1, 0): (6, 1),
        (1, 1): (2, 1),
        (1, 2): (3, 2),
        (1, 3): (5, 1),
        (3, 0): (1, 0),
        (3, 1): (2, 0),
        (3, 2): (4, 2),
        (3, 3): (5, 2),
        (6, 0): (5, 0),
        (6, 1): (4, 0),
        (6, 2): (2, 2),
        (6, 3): (1, 2),
        (2, 0): (6, 0),
        (2, 1): (4, 3),
        (2, 2): (3, 3),
        (2, 3): (1, 3),
        (5, 0): (3, 1),
        (5, 1): (4, 1),
        (5, 2): (6, 2),
        (5, 3): (1, 1),
    }[(region, d)]

    nr, nc = new_coords(rr, rc, d, nd)
    assert 0 <= nr < CUBE and 0 <= nc < CUBE
    nr, nc = region_to_global(nr, nc, newRegion)
    assert BOARD[nr][nc] in [".", "#"], f"{BOARD[nr][nc]}"
    return (nr, nc, nd)


def solve(part):
    r = 0
    c = 0
    d = 1
    while BOARD[r][c] != ".":
        c += 1

    i = 0
    while i < len(PATH):
        n = 0
        while i < len(PATH) and PATH[i].isdigit():
            n = n * 10 + int(PATH[i])
            i += 1
        for _ in range(n):
            rr = (r + DIRECTIONS[d][0]) % ROWS
            cc = (c + DIRECTIONS[d][1]) % COLS
            if BOARD[rr][cc] == " ":
                (nr, nc, nd) = get_dest(r, c, d, part)
                if BOARD[nr][nc] == "#":
                    break
                (r, c, d) = (nr, nc, nd)
                continue
            elif BOARD[rr][cc] == "#":
                break
            else:
                r = rr
                c = cc
        if i == len(PATH):
            break
        turn = PATH[i]
        if turn == "L":
            d = (d + 3) % 4
        elif turn == "R":
            d = (d + 1) % 4
        i += 1
    DV = {0: 3, 1: 0, 2: 1, 3: 2}
    return (r + 1) * 1000 + (c + 1) * 4 + DV[d]


print(solve(1))
print(solve(2))
