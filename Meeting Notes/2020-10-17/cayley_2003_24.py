"""Cayley 2003, Problem 24."""

from math import factorial


def comb(n: int, k: int) -> int:
    return factorial(n) // factorial(k) // factorial(n - k)


print("10 choose 4 =", comb(10, 4))

possibles = [(a, b, c, d)
             for a in range(10)
             for b in range(10)
             for c in range(10)
             for d in range(10)
             if a < b < c < d]

print("Number of possibles =", len(possibles))

solutions = [t for t in possibles if sum(t) % 3 == 0]

print("Number of solutions =", len(solutions))