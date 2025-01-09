def make_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15