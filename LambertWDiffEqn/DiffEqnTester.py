import numpy as np
import matplotlib.pyplot as plt
from DiffEqnSolvers import EulerTrap


def g(x, y):
    return y*np.sin(x*y)*np.exp(-x*y)


step = 100000
TrapIter = 5

x_0 = 0
y_0 = 10
End = 10

x_2, y_2 = EulerTrap(g, x_0, y_0, End, step, TrapIter)

x_2 = np.array(x_2)
y_2 = np.array(y_2)

x = np.linspace(x_0, End, step)


def Approximator(x, y_0):
    L = y_0 + 0.5 - 1/(8*y_0)
    return L - np.exp(-x*L) * np.sin(x*L + np.pi/4) / np.sqrt(2)


plt.title("Derived L Value")
plt.plot(x_2, y_2, label=f"EulerTrap {TrapIter}")
plt.plot(x, Approximator(x, y_0), label="Aprx")
plt.legend()
plt.savefig("graph2.png", dpi=1000)
