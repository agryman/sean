"""This module solves Galois 2020, #3."""


def is_rad_pair(a: int, b: int) -> bool:
    """Return True if and only if the pair (a, b) is a RadPair."""

    assert type(a) == int
    assert type(b) == int

    assert 1 <= a <= b <= 9

    ab = a * b
    ones_digit_ab = ab % 10
    tens_digit_ab = ab // 10

    d_exists: bool = False
    for d in range(1, 10):
        p = (a + d) * (b + d)
        ones_digit_p = p % 10
        tens_digit_p = p // 10

        d_exists = \
            p <= 99 and \
            ones_digit_p == d + ones_digit_ab and \
            tens_digit_p == d + tens_digit_ab

        if d_exists:
            break

    return d_exists


print(2, 5, is_rad_pair(2, 5))
print(2, 8, is_rad_pair(2, 8))
print(3, 6, is_rad_pair(3, 6))
