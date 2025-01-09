my_array = np.array([1, 2, 3, 4, 5])
#Choose one random element from my_array
random_element = np.random.choice(my_array)
print(random_element)

#Choose 3 random elements with replacement
random_elements_replacement = np.random.choice(my_array, size=3, replace=True)
print(random_elements_replacement)

#Choose 3 random elements without replacement
random_elements_no_replacement = np.random.choice(my_array, size=3, replace=False)
print(random_elements_no_replacement)
