# FLAME Assignment — Parametric Curve Fitting

## Links
- Desmos Graph: [https://www.desmos.com/calculator/8mn1tfkzmp](https://www.desmos.com/calculator/8mn1tfkzmp)

---

## Summary
This repository contains code and results for estimating unknown parameters in a given parametric curve using the provided `xy_data.csv`.  
The goal was to determine the parameters θ, M, and X that best fit the observed data points.

---

## Final Estimated Parameters
- θ (theta) = 28.118401° (≈ 0.49076 rad)  
- M = 0.021388  
- X = 54.901879

---

## Final Parametric Expression (LaTeX)
You can copy and paste this expression directly into a LaTeX document or Desmos:

```latex
\left(
t\cdot\cos(0.49076) - e^{0.021388\left|t\right|}\cdot\sin(0.3t)\sin(0.49076) + 54.901879,\;
42 + t\cdot\sin(0.49076) + e^{0.021388\left|t\right|}\cdot\sin(0.3t)\cos(0.49076)
\right)



##Files included

1)fit_curve.py — Python script used to fit the curve
2)xy_data.csv — input dataset (provided)
3)estimated_params.txt — numerical results (θ, M, X)
4)fit_plot.png — plot of data points and fitted curve
4)README.md — (this file)

## How I did it (short)

1. Created a uniform parameter vector **t** from 6 to 60 (the CSV has no `t` column).

2. Implemented the parametric model equations:

   \[
   x(t) = t \cdot \cos(\theta) - e^{M|t|} \cdot \sin(0.3t) \cdot \sin(\theta) + X
   \]

   \[
   y(t) = 42 + t \cdot \sin(\theta) + e^{M|t|} \cdot \sin(0.3t) \cdot \cos(\theta)
   \]

3. Defined an **L1 error** (mean absolute difference between predicted and observed `(x, y)` values).

4. Used **SciPy minimize (L-BFGS-B)** optimization method with bounds to estimate **θ**, **M**, and **X**.

5. Saved the results in `estimated_params.txt` and generated `fit_plot.png` showing both raw data and fitted curve.

##How to reproduce

1)Install Python 3.x and create/activate a virtual environment (optional).
2)Install the required packages:
3pip install numpy pandas scipy matplotlib

Run:

4)python fit_curve.py
The script will produce estimated_params.txt and fit_plot.png.


Author

Sriram Kumaran S
FLAME Assignment — 2025
