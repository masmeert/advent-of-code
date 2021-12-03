from utils import find_combination, mul

with open("2020/inputs/day01") as f:
    DATA = [int(x) for x in f.readlines()]


print(mul(find_combination(DATA, 2, 2020)))
print(mul(find_combination(DATA, 3, 2020)))
