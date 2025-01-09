def describe_pet(animal_type, pet_name, age=None):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    if age:
        print(f"My {animal_type} is {age} years old.")


describe_pet('hamster', 'harry', age=2) #Correct
#describe_pet(pet_name='harry', 'hamster', age=2) #Incorrect - Positional arguments must come before keyword arguments.
