import numpy as np
import matplotlib.pyplot as plt

# Define stepsize
step = 0.00001
N = int(np.ceil((1-0)/step))
x = np.linspace(0, 1, N)
psi_soln = [0]

# Left end boundary condition
psi = 0
# Derivative guess, doesn't matter when normalised
psi_prime = 1

# eigenvalue guess
n = 5
K = -(n*np.pi)**2

# Apply Euler's method to solve differential equation
for i in range(N-1):
    psi_double_prime = K * psi
    psi_prime = psi_prime + step * psi_double_prime
    psi = psi + step*psi_prime + step*step/2 * psi_double_prime
    psi_soln.append(psi)


psi_soln = np.array(psi_soln)
# Find modulus squared integral over region
psi_soln_mod_square = psi_soln**2
integral = np.sum(psi_soln**2) * step
psi_soln_mod_square = psi_soln_mod_square / integral
# Normalise wave function using sqrt of mod squared integral
psi_soln = psi_soln / np.sqrt(integral)
# Left End B.C
print(f"psi(0) = {psi_soln[0]}")
# Right End B.C
print(f"psi(1) = {psi_soln[psi_soln.size-1]}")
plt.plot(x, psi_soln_mod_square)

actual_soln = np.sin(n*np.pi*x)**2
actual_soln = actual_soln / (np.sum(actual_soln) * step)
plt.plot(x, actual_soln)
plt.show()

absolute_error = abs(actual_soln - psi_soln_mod_square)

plt.semilogy(x, absolute_error)