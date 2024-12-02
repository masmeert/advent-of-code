from utils import ALPHABET


def get_letter_index(letter: str) -> int:
    """Get the index of a letter in the alphabet.
    Args:
        letter (str): The letter to get the index of.
    Returns:
        int: The index of the letter.
    """
    return ALPHABET.index(letter) + 1
