import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: Read freefall.csv into arrays t and y
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: Compute velocity (v) and acceleration (a) using np.gradient
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {np.mean(a):.2f} m/s^2")
print(f"Acceleration std: {np.std(a):.2f}")

# TODO 3: Integrate acceleration back up to recover velocity and position
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_rec))
print(f"Max position difference: {max_diff:.4f} m")

# TODO 4: Create a 3-panel stacked plot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# 1. Position Panel
ax1.plot(t, y, label='Position (y)', color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion from Tracking Data')
ax1.grid(True)
ax1.legend()

# 2. Velocity Panel
ax2.plot(t, v, label='Velocity (v)', color='orange')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

# 3. Acceleration Panel
ax3.plot(t, a, label='Acceleration (a)', color='red', alpha=0.7)
ax3.axhline(-9.81, color='black', linestyle='--', label='-9.81 m/s² (ideal)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png')
print("Plot saved successfully as 'motion.png'!")