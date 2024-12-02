def get_input(day: str, split: str = "\n") -> list:
    """Get the input for a given day

    Args:
        day (int): the day to get the input for.
        split (str, optional): the string to split the input by. Defaults to "\n".

    Returns:
        list: the input for the given day.
    """
    with open(f"inputs/{day}.txt", "r") as f:
        return f.read().split(split)
