from utils import aoc


if __name__ == "__main__":
    guide = aoc.get_input("02")
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
    }  # Hardcoded from the input
    print(sum(scores[line][0] for line in guide))
    print(sum(scores[line][1] for line in guide))
