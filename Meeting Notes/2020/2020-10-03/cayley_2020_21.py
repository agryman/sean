"""Cayley 2020, Problem 21"""


def is_solution(x, y):
    return y == 4 * x + 3


def solutions():
    return [(x, y) for x in range(25, 76) for y in range(120, 251) if is_solution(x, y)]


s = solutions()
a = len(s)
print(f'Answer = {a}')
