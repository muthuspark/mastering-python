def calculate_sum(a, b):
    print(f"a: {a}, b: {b}") # Check input values
    sum = a + b
    print(f"Sum before return: {sum}") # Check result before return
    return sum

result = calculate_sum(5, 3)
print(f"Final Result: {result}")