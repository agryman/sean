"""Cayley 2020, Problem 23"""

import itertools

digits = [1, 1, 1, 2, 2, 2, 3, 3, 4]

unique_perms = {t for t in itertools.permutations(digits)}


def find(t, d):
    for i, x in enumerate(t):
        if x == d:
            return i

    return -1


def is_solution(t):

    # there is at least one 1 before the first 2
    i1 = find(t, 1)
    i2 = find(t, 2)
    if i1 > i2:
        return False

    # there is at least one 2 before the first 3
    i3 = find(t, 3)
    if i2 > i3:
        return False

    # there is at least one 3 before the first 4
    i4 = find(t, 4)
    if i3 > i4:
        return False

    # no digit 2 can be next to another 2
    for i in range(1, len(t)):
        if t[i] == 2 and t[i - 1] == 2:
            return False

    return True


def solutions():
    return [t for t in unique_perms if is_solution(t)]


s = solutions()
a = len(s)
print(f'Answer = {a}')
