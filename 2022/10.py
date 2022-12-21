from utils import aoc

if __name__ == "__main__":
    program = list(map(str.split, aoc.get_input("10")))

    register = [1]
    for instruction in program:
        register.append(register[-1])
        if instruction[0] != "noop":
            register.append(register[-1] + int(instruction[1]))

    print(sum(register[c - 1] * c for c in range(20, 221, 40)))

    screen = [[" "] * 40 for _ in range(6)]
    for i, x in enumerate(register):
        row = i // 40
        col = i % 40
        if abs(x - col) <= 1:
            screen[row][col] = "█"

    print("\n".join("".join(row) for row in screen))
