import numpy as np
from scipy.optimize import minimize, newton

# --- 2A: Convex Function f(x) = (x-3)^2 + 1 ---
def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def d2f(x):
    return 2.0

def gradient_descent(df_func, x0, alpha=0.1, max_iter=1000, tol=1e-6):
    x = x0
    for _ in range(max_iter):
        grad = df_func(x)
        if abs(grad) < tol:
            break
        x = x - alpha * grad
    return x

x0 = 0.0
gd_2a = gradient_descent(df, x0)
newton_2a = newton(df, x0, fprime=d2f)
slsqp_2a = minimize(f, x0, method="SLSQP").x[0]

print("=== 2A Results (Convex Function) ===")
print(f"Gradient Descent: x = {gd_2a:.4f}")
print(f"Newton Method:    x = {newton_2a:.4f}")
print(f"SLSQP:            x = {slsqp_2a:.4f}\n")


# --- 2B: Non-Convex Function g(x) = x^4 - 3x^2 + x + 5 ---
def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

def test_methods_2b(x_start):
    print(f"--- Starting point x0 = {x_start} ---")
    gd_res = gradient_descent(dg, x_start, alpha=0.01)
    
    try:
        newton_res = newton(dg, x_start, fprime=d2g)
        curvature = d2g(newton_res)
        curv_type = "Minimum (g'' > 0)" if curvature > 0 else "Maximum (g'' < 0)"
    except Exception as e:
        newton_res, curv_type = None, str(e)
        
    slsqp_res = minimize(g, x_start, method="SLSQP").x[0]

    print(f"Gradient Descent: x = {gd_res:.4f}")
    if newton_res is not None:
        print(f"Newton Method:    x = {newton_res:.4f} [{curv_type}]")
    print(f"SLSQP:            x = {slsqp_res:.4f}\n")

print("=== 2B Results (Harder Landscape) ===")
test_methods_2b(x_start=0.0)
test_methods_2b(x_start=2.0)