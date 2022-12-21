import operator
import sympy
from utils import aoc


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}
MONKEYS = {
    x[0]: x[1].split(" ")
    for x in (line.strip().split(": ") for line in aoc.get_input("21"))
}


def part_one(monkey):
    monkey_num = MONKEYS[monkey]
    if len(monkey_num) == 1:
        return int(monkey_num[0])
    else:
        op = monkey_num[1]
        a = part_one(monkey_num[0])
        b = part_one(monkey_num[2])

        return OPERATORS[op](a, b)


def get_equality(monkey):
    if monkey == "humn":
        return "x"

    monkey_num = MONKEYS[monkey]
    if len(monkey_num) == 1:
        return monkey_num[0]
    else:
        op = monkey_num[1]

        a = get_equality(monkey_num[0])
        b = get_equality(monkey_num[2])

        return f"({a}) {op} ({b})"


def part_two():
    a = get_equality(MONKEYS["root"][0])
    b = get_equality(MONKEYS["root"][2])
    x = sympy.symbols("x")

    A = sympy.parse_expr(a, local_dict={"x": x})
    B = sympy.parse_expr(b, local_dict={"x": x})

    return int(sympy.solve(sympy.Eq(A, B))[0])


if __name__ == "__main__":
    print(part_one("root"))
    print(part_two())
