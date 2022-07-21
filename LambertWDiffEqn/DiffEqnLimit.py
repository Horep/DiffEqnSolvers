import numpy as np
from scipy.special import lambertw
import matplotlib.pyplot as plt
from DiffEqnSolvers import EulerTrap


def g(x, y):
    return y*np.sin(x*y)*np.exp(-x*y)


step = 10000
TrapIter = 5

Start = 0
End = 200
subdiv = 1000+1
x = np.linspace(0, 5, subdiv)
list = []


for i in range(0, subdiv):
    x_2, y_2 = EulerTrap(g, Start, x[i], End, step, TrapIter)
    list.append(y_2[step])

list = np.array(list)
plt.plot(x, list, label="Euler Trap 5", linewidth=1)
L_a = 1/(2*lambertw(1/(2*x)))
plt.plot(x, L_a, label="Lambert Approx", linewidth=1)
plt.xlabel("y_0")
plt.ylabel("L(y_0)")
plt.legend()
plt.savefig("graph2.png", dpi=1000)
plt.cla()

plt.plot(x, abs(L_a-list), label="Error", linewidth=1)
plt.xlabel("y_0")
plt.ylabel("|L(y_0) - L_a|")
plt.legend()
plt.savefig("graph3.png", dpi=1000)
