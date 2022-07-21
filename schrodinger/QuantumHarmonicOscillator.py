import numpy as np
import matplotlib.pyplot as plt

# Energy Eigenvalue Guess
E = -90

step = 0.00001
N = int(np.ceil((1-0)/step))
x = np.linspace(0, 1, N)


def V(x):
    return x*x


def nrg_pot(x):
    return E - V(x)


# Boundary Conditions
psi_0 = 0
psi_prime_0 = 1

soln = np.zeros(N)
soln_d = np.zeros(N)
soln_dd = np.zeros(N)
soln[0] = psi_0
soln_d[0] = psi_prime_0
soln_dd[0] = nrg_pot(x[0])*psi_0




for i in range(N-1):
    soln_dd[i] = nrg_pot(x[i])*soln[i]
    soln_d[i+1] = soln_d[i] + step*soln_dd[i]
    soln[i+1] = soln[i] + step*soln_d[i] + step*step/2 * soln_dd[i]

print(f"psi(1) = {soln[N-1]}")
soln = np.array(soln)

integral = np.sum(soln*soln) * step

soln_squared = soln*soln / integral

plt.plot(x, soln_squared)
