from ..utils.advent import find_combination, prod

with open("2020/inputs/day01") as f:
    DATA = [int(x) for x in f.readlines()]


print(prod(find_combination(DATA, 2, 2020)))
print(prod(find_combination(DATA, 3, 2020)))
