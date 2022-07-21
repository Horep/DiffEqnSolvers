import numpy as np
import matplotlib.pyplot as plt

# Solves y' = f(x,y)
# Initial condition y(x_0) = y_0
# b is end point for solver

def Euler(f, x_0, y_0, b, step):
    h = (b - x_0) / step

    y = y_0
    x = x_0
    y_array = [y_0]
    x_array = [x_0]
    for i in range(step):
        y = y + h * f(x, y)
        x = x + h
        y_array.append(y)
        x_array.append(x)
    return x_array, y_array


def EulerTrap(f, x_0, y_0, b, step, Iter):
    h = (b - x_0) / step

    y = y_0
    x = x_0
    y_array = [y_0]
    x_array = [x_0]
    for i in range(step):
        y_p = y + h*f(x,y)
        
        for j in range(Iter):
            y_p = y + h/2 * (f(x, y) + f(x + h, y_p) )
        y = y_p
        x = x + h
        y_array.append(y)
        x_array.append(x)
    return x_array, y_array