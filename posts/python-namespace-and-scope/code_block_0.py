global_var = 10

def my_function():
    # Local namespace
    local_var = 5
    print(f"Inside function: global_var = {global_var}, local_var = {local_var}")

my_function()  # Output: Inside function: global_var = 10, local_var = 5
print(f"Outside function: global_var = {global_var}") # Output: Outside function: global_var = 10
#print(local_var) # This will raise a NameError because local_var is not in the global scope
