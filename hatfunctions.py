import numpy as np


def phi(x, x0, x1, x2):  # evaluated at x, evaluates to piecewise linear on [xim1,xi] and [xi,xip1]
    if x0 <= x <= x1:
        return (x - x0) / (x1 - x0)
    elif x1 <= x <= x2:
        return (x2 - x) / (x2 - x1)
    else:
        return 0


def phi_prime(x, x0, x1, x2):  # evaluated at x, evaluates to piecewise constant on [xim1,xi] and [xi,xip1]
    if x0 <= x <= x1:
        return 1 / (x1 - x0)
    elif x1 <= x <= x2:
        return -1 / (x2 - x1)
    else:
        return 0
