"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""

import argparse


def multiple_of_three_or_five(i: int) -> bool:
    """Return True if `i` is a multiple of 3 or 5 and False otherwise."""

    return i % 3 == 0 or i % 5 == 0


def sum_of_multiples(n: int) -> int:
    """Return the sum of all the multiples of 3 or 5 below `n`."""
    return sum(filter(multiple_of_three_or_five, range(n)))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Find the sum of all the multiples of 3 or 5 below N",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-n", type=int, default=1000, help="Ceiling for finding the sum"
    )
    args = parser.parse_args()
    print(sum_of_multiples(args.n))
