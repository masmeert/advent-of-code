with open("2021/inputs/day08.txt") as f:
    DATA = [[y.strip() for y in x.strip().split("|")] for x in f.readlines()]
for x in DATA:
    print(x)

def part_one() -> int:
    return sum(sum(len(y) in {2, 4, 3, 7} for y in x[1]) for x in DATA)


def part_two() -> int:
    """
    https://www.reddit.com/r/adventofcode/comments/rbj87a/comment/hnoyy04/?utm_source=share&utm_medium=web2x&context=3
    """
    s = 0
    for line in DATA:
        x,y = line
        l = {len(s): set(s) for s in x.split()}
        n = ''
        for o in map(set, y.split()):
            match len(o), len(o&l[4]), len(o&l[2]):  
                case 2,_,_: n += '1'
                case 3,_,_: n += '7'
                case 4,_,_: n += '4'
                case 7,_,_: n += '8'
                case 5,2,_: n += '2'
                case 5,3,1: n += '5'
                case 5,3,2: n += '3'
                case 6,4,_: n += '9'
                case 6,3,1: n += '6'
                case 6,3,2: n += '0'
        s += int(n)
    return s


print(part_one())
print(part_two())
