derivative = np.polyder(coefficients) #Result will be [6, 2] representing 6x + 2
print(f"The derivative of the polynomial is: {derivative}")

#Calculate second derivative
second_derivative = np.polyder(coefficients, 2) #Result will be [6] representing 6
print(f"The second derivative of the polynomial is: {second_derivative}")
