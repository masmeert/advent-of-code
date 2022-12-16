import numpy as np


def get_score(trees, tree_height):
    if all(tree_height > tree for tree in trees):
        return len(trees)
    for index, value in enumerate(trees):
        if value >= tree_height:
            return index + 1


def part1(file):
    lines = file.split("\n")
    forest_height = len(lines)
    forest_width = len(lines[0])
    forest = np.array(list(file.replace("\n", "")), "uint8").reshape(
        forest_height, forest_width
    )
    tree_height = -1
    trees_visible = 2 * forest_height + 2 * forest_width - 4
    for row in range(1, forest_height - 1):
        for col in range(1, forest_width - 1):
            tree_height = forest[row][col]

            up = forest[:, col][0:row]
            if tree_height > np.amax(up):
                trees_visible += 1
                continue

            down = forest[:, col][row:][1:]
            if tree_height > np.amax(down):
                trees_visible += 1
                continue

            left = forest[row][0:col]
            if tree_height > np.amax(left):
                trees_visible += 1
                continue

            right = forest[row][col:][1:]
            if tree_height > np.amax(right):
                trees_visible += 1
                continue
    return trees_visible


def part2(file):
    lines = file.split("\n")
    forest_height = len(lines)
    forest_width = len(lines[0])
    forest = np.array(list(file.replace("\n", "")), "uint8").reshape(
        forest_height, forest_width
    )

    max_score = -1
    for row in range(0, forest_height):
        for col in range(0, forest_width):
            tree_height = forest[row][col]
            score = 1

            up = np.flip(forest[:, col][0:row])
            score *= get_score(up, tree_height)

            down = forest[:, col][row:][1:]
            score *= get_score(down, tree_height)

            left = np.flip(forest[row][0:col])
            score *= get_score(left, tree_height)

            right = forest[row][col:][1:]
            score *= get_score(right, tree_height)

            max_score = max(score, max_score)
    return max_score


if __name__ == "__main__":
    file = open("inputs/08.txt").read()
    print(part1(file))
    print(part2(file))
