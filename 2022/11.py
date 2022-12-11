from copy import deepcopy
from operator import add, mul, attrgetter
from math import lcm, prod
import re


class Monkey:
    def __init__(self, data):
        regex = re.compile(r"\d+")
        matches = regex.findall(data[2])

        self.items = list(map(int, regex.findall(data[1])))
        self.operator = add if "+" in data[2] else mul
        self.operation_value = int(matches[0]) if matches else None
        self.divisible_by = int(regex.findall(data[3])[0])
        self.if_true = int(regex.findall(data[4])[0])
        self.if_false = int(regex.findall(data[5])[0])
        self.counter = 0

    def inspect(self):
        i = self.items.pop(0)
        if self.operation_value:
            return self.operator(i, self.operation_value)
        return self.operator(i, i)


def simulate(monkeys: list, rounds: int, p2=False):
    if p2:
        mod = prod(monkey.divisible_by for monkey in monkeys)

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.counter += len(monkey.items)

            while monkey.items:
                if p2:
                    item = monkey.inspect() % mod
                else:
                    item = monkey.inspect() // 3

                if item % monkey.divisible_by == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)

    a, b = sorted(map(attrgetter("counter"), monkeys), reverse=True)[:2]
    return a * b


if __name__ == "__main__":
    regex = re.compile(r"\d+")
    input = open("inputs/11.txt").read().split("\n\n")
    monkeys = []
    for block in input:
        data = block.split("\n")
        monkeys.append(Monkey(data))

    monkeys_copy = deepcopy(monkeys)
    print(simulate(monkeys, 20))
    print(simulate(monkeys_copy, 10000, True))
