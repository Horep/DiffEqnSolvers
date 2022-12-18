import numpy as np
import matplotlib.pyplot as plt
from basisfunctions import phi
import scipy
M = 5  # number of basis elements
h = 1/(M+1)  # distance between nodes
x = np.linspace(0, 1)


for k in range(1, M+1):
    y = [phi(xn, k, h) for xn in x]
    plt.plot(x, y)

A = np.zeros((M, M))

for i in range(M):  # fill stiffness matrix
    for j in range(M):
        if abs(i-j) <= 1:
            if i == j:
                A[i][j] = 24
            else: A[i][j] = -12
    A = A/h**3

b = np.zeros((M, 1))

for j in range(M):  # fill force vector
    b[i] = scipy.integrate.quad(phi, 0, 1, args=(j, h))

print(A)
print(b)
plt.show()
