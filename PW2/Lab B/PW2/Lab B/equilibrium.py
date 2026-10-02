import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar, minimize

K = 50.0

def k_imbalance(x):
    return ((2*x)**2) / ((1 - x) * (1 - x)) - K

def sq_imbalance(x):
    return k_imbalance(x[0])**2

# x-i [0, 0.999] aralığında məhdudlaşdırırıq (Brent metodu ilə)
sol = root_scalar(k_imbalance, bracket=[0.001, 0.999], method='brentq')
x_newton = sol.root

res_slsqp = minimize(sq_imbalance, x0=[0.5], method="SLSQP", bounds=[(0.001, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium extent (Brent/Newton): x = {x_newton:.4f}")
print(f"Equilibrium extent (SLSQP):        x = {x_slsqp:.4f}")

n_H2 = 1 - x_newton
n_I2 = 1 - x_newton
n_HI = 2 * x_newton

print(f"Equilibrium amounts: H2 = {n_H2:.4f} mol, I2 = {n_I2:.4f} mol, HI = {n_HI:.4f} mol")

x_vals = np.linspace(0, 0.95, 200)
nH2_vals = 1 - x_vals
nI2_vals = 1 - x_vals
nHI_vals = 2 * x_vals

plt.figure(figsize=(7, 5))
plt.plot(x_vals, nH2_vals, label="H2", color="blue")
plt.plot(x_vals, nI2_vals, label="I2", linestyle="--", color="green")
plt.plot(x_vals, nHI_vals, label="HI", color="red")
plt.axvline(x=x_newton, color="black", linestyle=":", label=f"Equilibrium (x = {x_newton:.2f})")
plt.xlabel("Extent of reaction (x)")
plt.ylabel("Amount (mol)")
plt.title("Chemical Equilibrium: H2 + I2 <=> 2HI")
plt.legend()
plt.grid(True)
plt.savefig("equilibrium.png")
plt.close()
