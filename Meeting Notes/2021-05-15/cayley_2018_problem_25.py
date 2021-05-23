"""
Cayley 2018, Problem 25
"""


def is_solution(x:int, y:int) -> bool:
    """Returns try if (x, y) is a solution."""

    # x and y are the values in a sequence of 15 terms of the following form:
    # xxxxyxxxxxyxxxx

    # x must be a positive integer
    if x <= 0:
        return False

    # y must be a negative integer
    if y >= 0:
        return False

    # a run of 6 consecutive terms must be positive
    if 5 * x + y <= 0:
        return False

    # a run of 11 consecutive terms must be negative
    if 9 * x + 2 * y >= 0:
        return False

    # x must be <= 16 or y must be >= 16
    return x <= 16 or y >= -16


solutions = [(x, y) for x in range(1, 101) for y in range(-100, 0) if is_solution(x, y)]

xs = {x for (x, y) in solutions}

xy_dict = { x: {y for (z, y) in solutions if z == x} for x in xs}
