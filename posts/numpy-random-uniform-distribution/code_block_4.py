np.random.seed(42) # Set the seed for reproducibility
random_numbers = np.random.uniform(size=5)
print(random_numbers)

np.random.seed(42) # Same seed, same results
random_numbers_again = np.random.uniform(size=5)
print(random_numbers_again)