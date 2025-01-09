while True:
    try:
        age = int(input("Enter your age: "))
        if age >= 0:
            print("Your age is:", age)
            break
        else:
            print("Age cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a number.")