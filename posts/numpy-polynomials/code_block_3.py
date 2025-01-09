poly1 = np.array([1, 2]) #represents x + 2
poly2 = np.array([2, 1]) #represents 2x + 1
product = np.polymul(poly1, poly2) #result will represent 2x^2 + 5x + 2
print(f"The product of the polynomials is: {product}")


#Divide two polynomials
dividend = np.array([2, 5, 2]) # represents 2x^2 + 5x +2
divisor = np.array([1, 2]) #represents x + 2
quotient, remainder = np.polydiv(dividend, divisor)
print(f"The quotient is: {quotient}") #Represents 2x + 1
print(f"The remainder is: {remainder}") #Represents 0
