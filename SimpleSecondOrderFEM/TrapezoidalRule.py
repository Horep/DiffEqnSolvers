import numpy as np


def trap_rule(f, a, b, n):
    interval = np.linspace(a, b, n+1)
    step_size = (b-a)/n
    sum = 0
    for k in range(1, n):
        sum += f(interval[k])
    sum += (f(a)+f(b))/2
    sum *= step_size
    return sum


def test_func(x):
    return np.sin(x)*x


#print(trap_rule(test_func, 0, 1))

