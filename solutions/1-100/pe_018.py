"""
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

     3
    7 4
   2 4 6
  8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below

https://projecteuler.net/problem=18
"""

from typing import List, Tuple, Optional


TRIANGLE = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 10],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def sum_of_max_route(
    triangle: List[List[int]], top_index: Optional[Tuple[int, int]] = (0, 0)
) -> int:
    """Return the sum of the max route of adjacent numbers in the `triangle`.

    Args:
        triangle: List of lists of ints representing a triangle
        top_index: Tuple of (row index, column index) to treat as the "top" of the triangle
    Returns:
        Sum of max route from `top_index` to base of `triangle`
    Raises:
        IndexError if an invalid `top_index` is provided given the dimensions of the `triangle`
    """

    row, col = top_index

    # In the base case, we are at the base of the triangle and the max sum is the current value
    max_sum = triangle[row][col]

    # If we have not reached the base of the triangle, the max sum is our current value plus the
    # The max of the max route to our left and the max route to our right.
    if len(triangle) > row + 1:
        max_sum += max(
            sum_of_max_route(triangle, (row + 1, col)),
            sum_of_max_route(triangle, (row + 1, col + 1)),
        )

    return max_sum


if __name__ == "__main__":
    print(sum_of_max_route(TRIANGLE))
