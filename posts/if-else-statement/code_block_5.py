temperature = 25
is_raining = True

if temperature > 20 and not is_raining:
    print("It's a beautiful day!")
elif temperature < 10 or is_raining:
    print("It's cold or rainy!")