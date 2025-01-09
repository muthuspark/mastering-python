np.random.seed(42) # Set the seed to 42
random_numbers = np.random.normal(loc=10, scale=3, size=5)
print(random_numbers)

np.random.seed(42) # Setting the same seed again
random_numbers_again = np.random.normal(loc=10, scale=3, size=5)
print(random_numbers_again) # Will be identical to the previous output