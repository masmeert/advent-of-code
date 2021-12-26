from typing import List

lines = open("2021/inputs/day04.txt").read().split("\n\n")
NUMS = map(int, lines[0].split(","))
BOARDS = [
    [
        tuple(int(x) for x in map(str.strip, row.split(" ")) if x)
        for row in line.split("\n")
    ]
    for line in lines[1:]
]


def solve() -> List[int]:
    seen, won, scores = set(), [], []
    for n in NUMS:
        seen.add(n)
        for board in BOARDS:
            col_and_rows = board + list(zip(*board))
            for line in col_and_rows:
                if all(num in seen for num in line) and board not in won:
                    won.append(board)
                    scores.append(
                        sum(
                            sum(num for num in line if num not in seen)
                            for line in board
                        )
                        * n
                    )
    return scores


result = solve()
print(result[0])
print(result[-1])
