try:
    age = int(input("Enter your age: "))
    if 0 < age < 120:
        print("Valid age")
    else:
        print("Invalid age")
except ValueError:
    print("Invalid input. Please enter an integer.")
