from utils import aoc


def snafu_to_int(snafu: str) -> int:
    num = 0
    place = 1
    for char in snafu[::-1]:
        match char:
            case "=":
                num += place * -2
            case "-":
                num += place * -1
            case _:
                num += place * int(char)
        place *= 5

    return num


def int_to_snafu(num: int) -> str:
    snafu = ""
    while num > 0:
        match num % 5:
            case 4:
                snafu += "-"
                num += 1
            case 3:
                snafu += "="
                num += 2
            case x:
                snafu += str(x)
        num //= 5
    return snafu[::-1]


if __name__ == "__main__":
    nums = aoc.get_input("25")
    total = sum(map(snafu_to_int, nums))
    print(int_to_snafu(total))
