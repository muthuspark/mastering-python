def describe_pet(animal_type, pet_name, age=None):
  """Displays information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")
  if age:
    print(f"My {animal_type} is {age} years old.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog', age=5)