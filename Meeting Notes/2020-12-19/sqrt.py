"""Compute the square root of a number."""


def sqrt(x):
    y = (1 + x)/2
    tolerance = 1.0e-10
    for i in range(10):
        error = abs(y*y - x)
        print(i, y, y*y, error)
        if error <= tolerance:
            break
        # improve the accuracy of y
        y = (y + x/y)/2

    return y
