string_list = ["10", "20", "a", "40", "50"]
integer_list = []
for x in string_list:
    try:
        integer_list.append(int(x))
    except ValueError:
        print(f"Skipping '{x}' - not a valid integer")

print(integer_list)  # Output: [10, 20, 40, 50]