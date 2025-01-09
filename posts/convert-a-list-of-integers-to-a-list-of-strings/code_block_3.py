mixed_list = [10, 20, 'thirty', 40, 50]

string_list = []
for item in mixed_list:
    try:
        string_list.append(str(item))
    except ValueError:
        print(f"Skipping non-integer value: {item}")

print(string_list) # Output will vary depending on what you want to do with non-integer values