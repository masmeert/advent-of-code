from typing import Tuple


X1, X2, Y1, Y2 = 14, 50, -267, -225


def launch(v: Tuple[int], p: Tuple[int] = (0, 0)) -> int:
    vx, vy = v
    px, py = p
    if px > X2 or py < Y1:
        return 0
    elif px >= X1 and py <= Y2:
        return 1
    return launch((vx - (vx > 0), vy - 1), (px + vx, py + vy))


print(
    abs(Y1) * abs(Y1 + 1) // 2
)  # https://www.reddit.com/r/adventofcode/comments/ri9kdq/comment/hovzej7/
print(sum(launch((x, y)) for x in range(1, 1 + X2) for y in range(Y1, -Y1)))
