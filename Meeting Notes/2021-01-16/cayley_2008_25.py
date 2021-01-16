"""Cayley Contest 2008, #25."""

from math import factorial
from itertools import permutations


def solve():
    numbers = [1, 2, 3, 11, 12, 13, 14]
    y = [(a-b)**2 + (b-c)**2 + (c-d)**2 + (d-e)**2 +(e-f)**2 + (f-g)**2
         for a, b, c, d, e, f, g in permutations(numbers)]
    return sum(y) // factorial(7)


print(solve())
