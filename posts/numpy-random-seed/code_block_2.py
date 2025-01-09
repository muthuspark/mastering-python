from numpy.random import default_rng

rng = default_rng(seed=42)
random_numbers = rng.random(5)
print(random_numbers)