"""
A gozinta chain for n is a sequence {1,a,b,...,n} where each element properly divides the next.

There are eight gozinta chains for 12:
{1,12}, {1,2,12}, {1,2,4,12}, {1,2,6,12}, {1,3,12}, {1,3,6,12}, {1,4,12} and {1,6,12}.
Let g(n) be the number of gozinta chains for n, so g(12)=8.
g(48)=48 and g(120)=132.

Find the sum of the numbers n not exceeding 10**16 for which g(n)=n.

https://projecteuler.net/problem=548
"""

from functools import lru_cache
import math
from typing import Set


LIMIT = 10 ** 5
CACHE_SIZE = LIMIT


@lru_cache(maxsize=CACHE_SIZE)
def all_factors(n: int) -> Set[int]:
    """Return the set of factors for `n`, excluding `n`."""
    factors = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if not n % i:
            factors.update([i, n // i])

    return factors - {n}


@lru_cache(maxsize=CACHE_SIZE)
def num_gozinta_chains(n: int) -> int:
    """Return the number of gozinta chains for n.

    Each unique chain for `n` corresponds to a unique chain
    for a factor `n`, with `n` added to the end of the chain.

    Therefore, the number of chains for `n` is sum of the
    number of chain for the factors of `n`.

    The count is more efficient to compute than the chains themselves.
    """
    return sum(num_gozinta_chains(k) for k in all_factors(n)) or 1


def perfect_gozinta(n: int) -> bool:
    """Return True if g(n)=n. Return False otherwise."""
    return num_gozinta_chains(n) == n


def sum_of_perfect_gozinta(limit: int) -> int:
    """Return the sum of the numbers n not exceeding `limit` for which g(n)=n."""
    return sum(filter(perfect_gozinta, range(1, limit)))


if __name__ == "__main__":
    print(sum_of_perfect_gozinta(LIMIT))
