import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titration.csv")
V = df["volume"].values
pH = df["pH"].values

dpH_dV = np.gradient(pH, V)

idx_eq = np.argmax(dpH_dV)
V_eq = V[idx_eq]
pH_eq = pH[idx_eq]

print(f"Equivalence Point: V = {V_eq:.2f} mL (pH = {pH_eq:.2f})")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, color="purple", linewidth=2)
ax1.axvline(V_eq, color="red", linestyle="--", label=f"Equiv Point ({V_eq:.1f} mL)")
ax1.set_xlabel("Volume of Base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.legend()
ax1.grid(True)

ax2.plot(V, dpH_dV, color="orange", linewidth=2)
ax2.axvline(V_eq, color="red", linestyle="--", label=f"Peak Slope ({V_eq:.1f} mL)")
ax2.set_xlabel("Volume of Base (mL)")
ax2.set_ylabel("dpH / dV")
ax2.set_title("First Derivative (dpH/dV)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("titration.png")
plt.close()