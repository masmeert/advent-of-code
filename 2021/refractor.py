from typing import List


def count_increases(data: List[int], step: int) -> int:
    """
    DAY01 part 1 & 2
    """
    if step < 0:
        return -1
    return sum(data[n] > data[n - step] for n in range(step, len(data)))