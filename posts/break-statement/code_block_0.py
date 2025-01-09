my_list = [10, 20, 30, 40, 50]
target_number = 30

for number in my_list:
    if number == target_number:
        print(f"Found {target_number}!")
        break  # Exits the loop immediately after finding the target
    print(f"Checking {number}...")

print("Loop finished.")