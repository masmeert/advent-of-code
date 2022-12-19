from utils import arrays, aoc, strings


def part_one(rucksacks: list[str]) -> list[int]:
    index_sum = 0
    for rucksack in rucksacks:
        compartments = arrays.split_at(rucksack, len(rucksack) // 2)
        intersection = arrays.get_intersection(compartments)

        intersection_index = strings.get_letter_index(
            *intersection
        )  # Intersection is a single element set
        index_sum += intersection_index

    return index_sum


def part_two(rucksacks: list[str]) -> list[int]:
    index_sum = 0
    for i in range(0, len(rucksacks), 3):
        compartments = rucksacks[i : i + 3]
        intersection = arrays.get_intersection(compartments)

        intersection_index = strings.get_letter_index(*intersection)
        index_sum += intersection_index

    return index_sum


if __name__ == "__main__":
    rucksacks = aoc.get_input("03")
    print(part_one(rucksacks))
    print(part_two(rucksacks))
