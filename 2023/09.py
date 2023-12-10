def read_input(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        return [list(map(int, line.split())) for line in f.readlines()]


def extrapolate(history: list[int]):
    if sum(value != 0 for value in history) == 0:
        return 0
    extrapolated = [
        history[index + 1] - history[index] for index in range(len(history) - 1)
    ]
    return history[-1] + extrapolate(extrapolated)


if __name__ == "__main__":
    readings = read_input("inputs/09.txt")
    print(sum(extrapolate(history) for history in readings))
    print(sum(extrapolate(history[::-1]) for history in readings))
