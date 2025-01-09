from scipy import integrate
import numpy as np

def f(x):
  return np.sin(x)

result, error = integrate.quad(f, 0, np.pi)
print(f"The integral is: {result}, with an estimated error of: {error}")