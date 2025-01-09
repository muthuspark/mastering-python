x = 2
result = np.polyval(coefficients, x)  #result will be 17 (3*2^2 + 2*2 + 1)
print(f"The value of the polynomial at x = {x} is: {result}")


x_values = np.array([0, 1, 2, 3])
results = np.polyval(coefficients, x_values)
print(f"The values of the polynomial at x = {x_values} are: {results}")