ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_letter_index(letter):
    return ALPHABET.index(letter) + 1


def part1(rucksacks):
    letters = []
    for rucksack in rucksacks:
        a = rucksack[: len(rucksack) // 2]
        b = rucksack[len(rucksack) // 2 :]
        intersection = set(a) & set(b)
        letters.append(*intersection)

    return letters


def part2(rucksacks):
    letters = []
    for i in range(0, len(rucksacks), 3):
        a, b, c = rucksacks[i : i + 3]
        intersection = set(a) & set(b) & set(c)
        letters.append(*intersection)

    return letters


if __name__ == "__main__":
    rucksacks = open("inputs/03.txt").read().split("\n")
    print(sum(map(get_letter_index, part1(rucksacks))))
    print(sum(map(get_letter_index, part2(rucksacks))))
