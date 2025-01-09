np.random.seed(42) #Sets the seed to 42
random_numbers = np.random.rand(5)
print(random_numbers)

np.random.seed(42) #Same seed, same output
random_numbers_again = np.random.rand(5)
print(random_numbers_again)