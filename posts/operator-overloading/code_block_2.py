class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __str__(self): #for better printing
        return f"{self.real} + {self.imag}j"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 1)

c3 = c1 + c2
c4 = c1 * c2

print(f"c1 + c2 = {c3}") # Output: c1 + c2 = 6 + 4j
print(f"c1 * c2 = {c4}") # Output: c1 * c2 = 5 + 14j
