import itertools
import heapq
import numpy
from typing import List, Optional, Tuple


FIGURES = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
VOWELS = ("a", "e", "i", "o", "u")
LETTERS = tuple(x for x in "abcdefghijklmnopqrstuvwxyz")
CONSONANTS = tuple(x for x in LETTERS if x not in VOWELS)


# * STRINGS/ARRAYS
def is_palyndrome(s: str) -> bool:
    """check if string is a palydrome

    Args:
        s (str): string to check

    Returns:
        bool: result
    """
    s = "".join(l.lower() for l in s if l.isalpha())
    return s == s[::-1]


def most_frequent(l: List[any]) -> any:
    """finds the most frequent item in a list

    Args:
        l (List[any]): a list

    Returns:
        any: the most frequent item
    """
    return max(set(l), key=l.count)


def find_combination(l: List[int], s: int, t: int) -> Optional[List[int]]:
    """Finds a combination from a list that sums up to a given total

    Args:
        l (List[int]): the list
        s (int): the size of the combination
        t (int): the sum of the combination we're looking for

    Returns:
        List[int] (defaults to None): the combination
    """
    pairs = itertools.combinations(l, s)
    for p in pairs:
        if sum(p) == t:
            return p
    return None


def largest(l: List[any], n: int) -> List[any]:
    """Finds the n largest elements in a list

    Args:
        l (List[any]): the list
        n (int): the amount of element to return

    Returns:
        List[any]: the n largest elements
    """
    return heapq.nlargest(n, l)


def smallest(l: List[any], n: int) -> List[any]:
    """Finds the n smallest elements in a list

    Args:
        l (List[any]): the list
        n (int): the amount of element to return

    Returns:
        List[any]: the n smallest elements
    """
    return heapq.nsmallest(n, l)


def first_occurence(l: List[any], e: any) -> int:
    """Finds the first occurence of an element in a list

    Args:
        l (List[any]): the list
        e (any): the element

    Returns:
        int (defaults to -1): index of its first occurences
    """
    return -1 if e is None else l.find(e)


def sort_by_nth_largest_item(l: List[List[int]], n: int) -> Tuple[int]:
    """Sorts a multi-dimensional list by the nth element of its sub lists

    Args:
        l (List[int]): the multi-dimensional list
        n (int): the index of the element to sort by

    Returns:
        Tuple[int]: the sorted list
    """
    return tuple(reversed(sorted(l, key=lambda x: x[n])))


def get_fist_unique(l: List[any]) -> int:
    """Returns the first unique element of a list

    Args:
        l (List[any]): the list

    Returns:
        int: the first unique
    """
    for x in l:
        if l.count(x) == 1:
            return l.index(x)
    return -1


# * MATH
def gaussian_sum(x: int) -> int:
    """Returns the gaussian summation for x

    Args:
        x (int): the num

    Returns:
        int: the gaussian sum

    https://letstalkscience.ca/educational-resources/backgrounders/gauss-summation
    """
    return x * (x + 1) // 2


def _eratosthenes(n: int) -> List[int]:
    """Computes n primes
    http://stackoverflow.com/a/3941967/239076
    """
    _primes = [True] * n
    _primes[0] = _primes[1] = False
    for i, is_prime in enumerate(_primes):
        if is_prime:
            yield i

            for j in range(i * i, n, i):
                _primes[j] = False


def primes(n: int) -> Tuple[int]:
    """Returns n primes

    Args:
        n (int): amount of primes to return

    Returns:
        Tuple[int]: n first primes
    """
    return tuple(_eratosthenes(n))


def get_evens(l: List[int]) -> List[int]:
    """Gets all even numbers in a list

    Args:
        l (List[int]): the list

    Returns:
        List[int]: all evens
    """
    return [x for x in l if x % 2 == 0]


def nth_fib(n: int) -> int:
    """Efficiencily computes nth fib number
    https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series/23462371#23462371
    """
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == "1":
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def get_sigmoid(x: int) -> float:
    """Gets the sigmoid of a num

    Args:
        x (int): the num

    Returns:
        float: its sigmoid
    """
    return 1.0 / (1 + numpy.exp(-x))


def to_32(x: int) -> int:
    """Converts an int to 32bits

    Args:
        x (int): the int

    Returns:
        int: its 32bits conversion
    """
    x = x % (2 ** 32)
    if x >= 2 ** 31:
        x = x - 2 ** 32
    x = int(x)
    return x


def is_power_of_two(x: int) -> bool:
    """checks if x is a power of two

    Args:
        x (int): the num

    Returns:
        bool: result
    """
    i = 1
    while i < x:
        i *= 2
    return i == x


def reverse_32bit(x: int) -> int:
    """Reverses a 32bit int

    Args:
        x (int): the 32bit int

    Returns:
        int: its reverse
    """
    if x == 0:
        return 0
    temp = str(x)
    if x < 0:
        temp = temp[1:].strip("0")
        ret = int("-" + temp[::-1])
    else:
        ret = int(temp.strip("0")[::-1])
    return ret if -2147483649 <= ret < 2147483649 else 0


def factors(x: int) -> List[int]:
    """Gets all factors of a num

    Args:
        x (int): the num

    Returns:
        List[int]: all its factors
    """
    return sorted(
        x
        for tup in ([i, x // i] for i in range(1, int(x ** 0.5) + 1) if x % i == 0)
        for x in tup
    )


def gcd(a: int, b: int) -> int:
    """Gets the greatest common divisor of two ints

    Args:
        a (int): first int
        b (int): second int

    Returns:
        int: the GCD
    """
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Gets the lowest common multiplicator of two ints

    Args:
        a (int): first int
        b (int): second int

    Returns:
        int: the LCM
    """
    return a * b / gcd(a, b)
