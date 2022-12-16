import re


def get_input():
    with open("inputs/16.txt") as f:
        lines = f.read().splitlines()

    valves = {}
    for line in lines:
        line = line.strip().split(" ")
        name = line[1]
        valves[name] = {
            "flow": int(line[4].split("=")[-1].split(";")[0]),
            "valves": [word.split(",")[0] for word in line[9:]],
        }

    return valves


if __name__ == "__main__":
    valves = get_input()
    print(valves)
