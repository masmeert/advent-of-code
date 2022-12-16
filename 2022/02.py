def get_input():
    guide = open("inputs/02.txt").read().split("\n")
    scores = {
        "A X": (4, 3),
        "A Y": (8, 4),
        "A Z": (3, 8),
        "B X": (1, 1),
        "B Y": (5, 5),
        "B Z": (9, 9),
        "C X": (7, 2),
        "C Y": (2, 6),
        "C Z": (6, 7),
    }

    return guide, scores


def play(guide, scores):
    score = 0
    score_part2 = 0

    for line in guide:
        score += scores[line][0]
        score_part2 += scores[line][1]

    return score, score_part2


if __name__ == "__main__":
    guide, scores = get_input()
    print(play(guide, scores))
