import numpy as np


def phi(x, j, h):
    if (j - 1) * h <= x <= j * h:
        return -(2 * x ** 3 - 3 * (2 * j - 1) * h * x ** 2 + 6 * (j - 1) * j * h ** 2 * x - (j - 1) ** 2 * (
                    2*j + 1) * h ** 3) / h ** 3
    elif j * h <= x <= (j + 1) * h:
        return (2 * x ** 3 - 3 * (2 * j + 1)*h*x**2 + 6*j*(j+1)*h**2*x - (j+1)**2*(2*j-1)*h**3)/h**3
    else:
        return 0


def phi_dd(x, j, h):
    if (j - 1) * h <= x <= j * h:
        return -(12 * x - 6 * (2 * j - 1) * h) / h ** 3
    elif j * h <= x <= (j + 1) * h:
        return (12 * x - 6 * (2 * j + 1)*h)/h**3
    else:
        return 0
