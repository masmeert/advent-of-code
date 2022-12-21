def get_intersection(arrays: list[list]) -> set:
    """Get the intersection of multiple arrays.

    Args:
        arrays (list[list]): The arrays to get the intersection of.

    Returns:
        set: The intersection of the arrays.
    """
    intersection = set(arrays[0])
    for array in arrays[1:]:
        intersection &= set(array)

    return intersection


def split_at(array: list, at: int) -> tuple[list]:
    """Split an array at a given index.

    Args:
        array (list): The array to split.
        at (int): The index to split at.

    Returns:
        tuple[list]: The split array.
    """
    return array[:at], array[at:]


def parseInts(array: list) -> list[int]:
    """Parse a list of strings to ints.

    Args:
        array (list): The array to parse.

    Returns:
        list[int]: The parsed array.
    """
    return list(map(int, array))
