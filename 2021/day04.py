from typing import List

with open("2021/inputs/day04.txt") as f:
    lines = f.read().split("\n\n")
    NUMS = map(int, lines[0].split(","))
    BOARDS = [
        [
            [int(x) for x in map(str.strip, row.split(" ")) if x]
            for row in line.split("\n")
        ]
        for line in lines[1:]
    ]


def solve() -> List[int]:
    seen = []
    won = []
    scores = []
    for n in NUMS:
        seen.append(n)
        for board in BOARDS:
            transpose = list(zip(*board))
            for i, line in enumerate(board):
                if (
                    all(num in seen for num in line)
                    or all(num in seen for num in transpose[i])
                ) and board not in won:
                    won.append(board)
                    scores.append(
                        sum(
                            sum(num for num in line if num not in seen)
                            for line in board
                        )
                        * seen[-1]
                    )
    return scores


scores = solve()
print("part1:", scores[0])
print("part2:", scores[-1])
