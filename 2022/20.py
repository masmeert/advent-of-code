def get_input():
    with open("inputs/20.txt") as f:
        return f.readlines()


def decrypt(nums: list[int], steps: int = 1) -> int:
    indices = list(range(len(nums)))

    for i in indices * steps:
        j = indices.index(i)
        indices.pop(j)
        indices.insert((j + nums[i]) % len(indices), i)

    zero = indices.index(nums.index(0))
    return sum(
        nums[indices[(zero + offset) % len(nums)]] for offset in (1000, 2000, 3000)
    )


if __name__ == "__main__":
    file = get_input()

    nums = [int(x) for x in file]
    print(decrypt(nums))

    nums = [int(x) * 811589153 for x in file]
    print(decrypt(nums, 10))
