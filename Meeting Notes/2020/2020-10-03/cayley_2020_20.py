"""Cayley 2020, Problem 20"""


def is_divisible(n, d):
    return (n % d) == 0


def solutions():
    a = range(1, 101)
    b = range(101, 206)
    return [(m, n) for m in a for n in b if is_divisible(3**m + 7**n, 10)]


s = solutions()
a = len(s)
print(f'Answer = {a}')