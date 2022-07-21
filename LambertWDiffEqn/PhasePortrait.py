import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return y * np.sin(x * y) * np.exp(-x * y)


fig = plt.figure()

x = np.linspace(0.0, 10, 10000)
y = np.linspace(0.0, 10, 10000)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.pcolormesh(X, Y, Z, cmap="inferno")
plt.colorbar(label="y'")
plt.ylabel("y")
plt.xlabel("x")
plt.savefig("ColourMesh.png", dpi=1000)
plt.show()
