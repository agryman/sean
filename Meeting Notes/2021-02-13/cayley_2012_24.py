"""Cayley 2012, Question 24"""

from itertools import permutations


def is_valid(s: tuple[int]) -> bool:
    n = len(s)
    return not any([i == s[s[i]] for i in range(n)])


def solve(n: int) -> int:
    solutions = [s for s in permutations(range(n)) if is_valid(s)]
    return len(solutions)
