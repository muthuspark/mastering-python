import numpy as np

x = 2
sinh_x = np.sinh(x)
cosh_x = np.cosh(x)
tanh_x = np.tanh(x)
print(f"sinh({x}): {sinh_x}")
print(f"cosh({x}): {cosh_x}")
print(f"tanh({x}): {tanh_x}")

x_array = np.array([1, 2, 3, 4, 5])
sinh_array = np.sinh(x_array)
cosh_array = np.cosh(x_array)
tanh_array = np.tanh(x_array)
print("\nHyperbolic functions on an array:")
print(f"sinh(x_array): {sinh_array}")
print(f"cosh(x_array): {cosh_array}")
print(f"tanh(x_array): {tanh_array}")


#Example using other hyperbolic functions
x_array2 = np.array([1, 2, 3])
coth_array = np.cosh(x_array2)/np.sinh(x_array2)
sech_array = 1/np.cosh(x_array2)
csch_array = 1/np.sinh(x_array2)
print("\nExample with coth, sech and csch:")
print(f"coth(x_array): {coth_array}")
print(f"sech(x_array): {sech_array}")
print(f"csch(x_array): {csch_array}")