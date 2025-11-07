import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("xy_data.csv")
x_data = data['x'].values
y_data = data['y'].values
t_vals = np.linspace(6, 60, len(x_data))

# Equation of curve
def curve(params, t):
    theta, M, X = params
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

# Error (L1 distance)
def error(params):
    x_pred, y_pred = curve(params, t_vals)
    return np.mean(np.abs(x_pred - x_data) + np.abs(y_pred - y_data))

# Initial guesses (within given ranges)
init = [np.deg2rad(25), 0.01, 50]

# Bounds: (theta in radians, M, X)
bounds = [(np.deg2rad(0), np.deg2rad(50)), (-0.05, 0.05), (0, 100)]

# Optimize
res = minimize(error, init, bounds=bounds, method='L-BFGS-B')
theta, M, X = res.x

# Save results
with open("estimated_params.txt", "w") as f:
    f.write(f"Theta (deg): {np.rad2deg(theta):.6f}\n")
    f.write(f"M: {M:.6f}\n")
    f.write(f"X: {X:.6f}\n")

# Plot data vs fit
x_fit, y_fit = curve(res.x, t_vals)
plt.figure(figsize=(6, 6))
plt.plot(x_data, y_data, 'o', label='Given Data')
plt.plot(x_fit, y_fit, '-', label='Fitted Curve')
plt.legend()
plt.title("Curve Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.tight_layout()
plt.savefig("fit_plot.png")
plt.close()

print("Done! Results saved to estimated_params.txt and fit_plot.png")
