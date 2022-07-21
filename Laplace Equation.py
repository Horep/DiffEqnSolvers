import numpy as np
import matplotlib.pyplot as plt
n = 500

grid = np.zeros((n, n))
f_opt = 2 - 2*np.pi / n
x = np.arange(1, n+1)
X, Y = np.meshgrid(x, x)


def laplace(u, u1, u2, u3, u4, u5, steps):

    def initial(j, i):
        if i == 0:
            return u1
        if i == n-1:
            return u2
        if j == 0:
            return u3
        if j == n-1:
            return u4
        else:
            return u5

    def next_xd(uc, un, us, ue, uw):
        res = (un + us + ue + uw)/4 - uc
        return uc + f_opt*res

    def newgrid():
        for i in range(0, n):
            for j in range(0, n):
                u[i, j] = initial(i, j)

    def relax(u):
        for b in range(0, 1+1):
            for i in range(1, n-1):
                k = (i+b) % 2
                j = 2 - k
                while j < n-k:
                    u[i, j] = next_xd(u[i, j], u[i-1, j], u[i+1, j], u[i, j+1],
                                      u[i, j-1])
                    j += 2
    newgrid()
    for k in range(0, steps):
        relax(u)
    return u


p = laplace(grid, 0.0, 100.0, 50, 0.0, 37.5, 2*n)
plt.pcolormesh(X, Y, p, cmap="inferno")
plt.colorbar()
plt.savefig("LaplaceSolutionSquare.png", dpi=1000)
plt.show()
