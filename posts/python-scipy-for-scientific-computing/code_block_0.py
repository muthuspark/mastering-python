import numpy as np
from scipy import optimize

def f(x):
  return x**2 + 2*x + 1

result = optimize.minimize_scalar(f)
print(result)