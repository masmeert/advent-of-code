import numpy as np
from typing import Tuple


def sigmoid(x: int) -> float:
    """Returns the sigmoid of x."""
    return 1.0 / (1 + np.exp(-x))


def gaussian_sum(x: int) -> int:
    """Returns the gaussian sum of x."""
    return x * (x + 1) // 2


def primes(n: int) -> Tuple[int]:
    """Computes n primes."""

    def _eratosthenes(n: int):
        """http://stackoverflow.com/a/3941967/239076"""
        primes = [True] * n
        primes[0] = primes[1] = False
        for i, is_prime in enumerate(primes):
            if is_prime:
                yield i
                for j in range(i * i, n, i):
                    primes[j] = False

    return tuple(_eratosthenes(n))


def nth_fib(n: int) -> int:
    """Efficiencily computes nth fib number.
    https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series/23462371#23462371
    """
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == "1":
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def factors(x: int) -> Tuple[int]:
    """Gets all factors of x."""
    return tuple(
        sorted(
            x
            for tup in ([i, x // i] for i in range(1, int(x**0.5) + 1) if x % i == 0)
            for x in tup
        )
    )


def gcd(a: int, b: int) -> int:
    """Gets the greatest common divisor of two ints."""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Gets the lowest common multiplicator of two ints."""
    return a * b / gcd(a, b)
