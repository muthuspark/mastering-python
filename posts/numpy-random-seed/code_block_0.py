import numpy as np

np.random.seed(42)

random_numbers = np.random.rand(5)
print(f"Random numbers with seed 42: {random_numbers}")

np.random.seed(100)

random_numbers_2 = np.random.rand(5)
print(f"Random numbers with seed 100: {random_numbers_2}")