x = 20  # Global scope

def outer_function():
    x = 30  # Enclosing function scope
    def inner_function():
        x = 40  # Local scope
        print(f"Inside inner: x = {x}")
    inner_function()
    print(f"Inside outer: x = {x}")

outer_function()
print(f"Outside functions: x = {x}")