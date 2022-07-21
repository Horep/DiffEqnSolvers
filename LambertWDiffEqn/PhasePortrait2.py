import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return y * np.sin(x * y) * np.exp(-x * y)


fig = plt.figure()

x = np.linspace(0.0, 10, 30)
y = np.linspace(0.0, 10, 20)

X, Y = np.meshgrid(x, y)


U = 1
V = f(X, Y)
# Normalize arrows
N = np.sqrt(U ** 2 + V ** 2)
U2, V2 = U/N, V/N
plt.quiver(X, Y, U2, V2)
plt.ylabel("y")
plt.xlabel("x")
plt.savefig("SlopeField.png", dpi=1000)
plt.show()
