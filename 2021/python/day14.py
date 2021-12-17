from collections import Counter
from itertools import count

RULES = {}
for x in open("2021/inputs/day14.txt").readlines():
    k, v = x.strip().split(" -> ")
    RULES[k] = v
TEMPLATE = "VPPHOPVVSFSVFOCOSBKF"


def solve(steps: int) -> int:
    pairs = Counter(TEMPLATE[i : i + 2] for i in range(len(TEMPLATE) - 1))
    for i in count():
        new_pairs = Counter()
        for pair, c in pairs.items():
            a, b = pair
            d = RULES[pair]
            new_pairs[a + d] += c
            new_pairs[d + b] += c
        pairs = new_pairs
        if i == steps - 1:
            elements = Counter()
            for pair, c in pairs.items():
                elements[pair[0]] += c
            elements[TEMPLATE[-1]] += 1  # too lazy to find the issue
            mc = elements.most_common()
            return mc[0][1] - mc[-1][1]


print(solve(10))
print(solve(40))
