import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data = pd.read_csv("kinetics.csv")
t_data = data["time"].values
C_data = data["concentration"].values

C0 = C_data[0]

def error_func(k):
    k_val = k[0]
    C_pred = C0 * np.exp(-k_val * t_data)
    return np.sum((C_data - C_pred)**2)

res = minimize(error_func, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
fitted_k = res.x[0]

print(f"Fitted rate constant k = {fitted_k:.4f}")

t_dense = np.linspace(min(t_data), max(t_data), 200)
C_dense = C0 * np.exp(-fitted_k * t_dense)

plt.figure(figsize=(7, 5))
plt.scatter(t_data, C_data, color="red", label="Measured Data")
plt.plot(t_dense, C_dense, color="blue", label=f"Fit: C(t) = C0 * e^(-{fitted_k:.2f}t)")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-Order Kinetics Fit")
plt.legend()
plt.grid(True)
plt.savefig("kinetics.png")
plt.close()