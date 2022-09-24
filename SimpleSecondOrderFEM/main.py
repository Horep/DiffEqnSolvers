import numpy as np
import matplotlib.pyplot as plt
from hatfunctions import phi, phi_prime
from TrapezoidalRule import trap_rule
M = 50  # number of non-boundary points
x = np.linspace(0, 1, M+2)

A = np.zeros((M, M))
b = np.zeros((M, 1))


# Solves -u'' = f, with u(0)=u(1)=0

def f(z):
    return z*np.exp(z)


for i in range(1, M+1):
    for j in range(i, M+1):
        if abs(i-j)>1:
            A[i-1,j-1]=0
        else:
            def integrand(z):
                return phi_prime(z, x[i-1], x[i], x[i+1])*phi_prime(z, x[j-1], x[j], x[j+1])
            A[i-1, j-1] = trap_rule(integrand, x[i-1], x[i+1], 3)  # uses 3 to get exact answer when integrating
            A[j - 1, i - 1] = A[i-1, j-1]


print(A*1/(M+1))
for i in range(1,M+1):
    def integrand(z):
        return phi(z, x[i - 1], x[i], x[i + 1]) * f(z)
    b[i-1] = trap_rule(integrand, 0, 1, 1000)


x_cont = np.linspace(0,1,100)  # real
coeff = np.linalg.solve(A, b)


def plot(z):
    sum = 0
    for i in range(1, M+1):
        sum+= coeff[i-1]*phi(z, x[i - 1], x[i], x[i + 1])
    return sum


def actual(z):
    return -np.exp(z)*(z-2) + 2*(z-1) - np.exp(1)*z

y = [plot(z) for z in x_cont]
y2 = actual(x_cont)
plt.plot(x_cont, y, label="FEM")
plt.plot(x_cont, y2, linestyle='--', label="Actual")
plt.legend()
plt.show()
