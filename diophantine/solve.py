"""This program solves the linear Diophantine equation ax + by = c where all variables are integers."""

from typing import Optional
from math import gcd

def solve(a: int, b: int, c: int) -> Optional[tuple[int, int]]:
    """Return (x,y) that satisfy ax + by = c or None if no solution exists."""

    if c == 0:
        return 0, 0

    assert c != 0

    if a == 0 and b == 0:
        return None

    if a == 0:
        assert b != 0
        y = c // b
        if b * y == c:
            return 0, y
        else:
            return None

    assert a != 0

    if b == 0:
        x = c // a
        if a * x == c:
            return x, 0
        else:
            return None

    assert b != 0

    if a < 0:
        solution = solve(-a, b, c)
        if solution is None:
            return None
        else:
            x1, y1 = solution
            x, y = -x1, y1
            assert a * x + b * y == c
            return x, y

    assert a > 0

    if b < 0:
        solution = solve(a, -b, c)
        if solution is None:
            return None
        else:
            x1, y1 = solution
            x, y = x1, -y1
            assert a * x + b * y == c
            return x, y

    assert b > 0

    if c < 0:
        solution = solve(a, b, -c)
        if solution is None:
            return None
        else:
            x1, y1 = solution
            x, y = -x1, -y1
            assert a * x + b * y == c
            return x, y

    assert c > 0

    d: int = gcd(a, b)
    assert d > 0
    if c % d != 0:
        return None

    if d > 1:
        a1 = a // d
        b1 = b // d
        c1 = c // d
        return solve(a1, b1, c1)

    assert d == 1
    # a and b are coprime.
    # Therefore we can solve the equation ax' + by' = 1.

    if c > 1:
        solution = solve(a, b, 1)
        assert solution is not None
        x1, y1 = solution
        x, y = c * x1, c * y1
        assert a * x + b * y == c
        return x, y

    assert c == 1
    # Solve ax + by = 1 where we know that a and b are coprime and positive

    if a == 1:
        return 1, 0

    assert a > 1

    if b == 1:
        return 0, 1

    assert b > 1
    assert a != b

    if a > b:
        solution = solve(b, a, 1)
        assert solution is not None
        x1, y1 = solution
        x, y = y1, x1
        assert a * x + b * y == 1
        return x, y

    assert a < b
    # write b = qa + r using integer division

    q: int = b // a
    assert q >= 1

    r: int = b % a
    assert 0 < r < a

    # ax + (qa+r)y = 1
    # ry + a(x + qy) = 1
    # (x', y') = (y, x + qy)
    # solve rx' + ay' = 1
    solution = solve(r, a, 1)
    assert solution is not None
    x1, y1 = solution
    x, y = y1 - q * x1, x1
    assert a * x + b * y == 1
    return x, y


print(solve(2, 4, 9))
