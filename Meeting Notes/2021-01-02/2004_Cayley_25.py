from math import gcd


def solve(x_max = 60, k_max = 300):
    return [x for x in range(1, 61) if lowest_terms(x, k_max)]


def lowest_terms(x: int, k_max: int) -> bool:
    return all([gcd(7 * x + k, k + 1) == 1 for k in range(1, k_max + 1)])