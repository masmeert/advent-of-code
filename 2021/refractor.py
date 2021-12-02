from typing import List, Tuple


def sonar_sweep(data: List[int], step: int) -> int:
    """
    DAY01 part 1 & 2
    """
    if step < 0:
        return -1
    return sum(data[n] > data[n - step] for n in range(step, len(data)))


def dive(data: List[Tuple[str, int]], part: int) -> int:
    """
    DAY02 part 1 & 2
    """
    fwd = depth = aim = 0
    for x in data:
        if x[0] == "forward":
            fwd += x[1]
            depth += x[1] * aim
        else:
            aim += -x[1] if x[0] == "up" else x[1]
    return fwd * (depth if part == 2 else aim)
