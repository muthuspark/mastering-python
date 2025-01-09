try:
    with open("my_file.txt", "w") as f:
        f.write("This is some text.")
        # ... other file operations ...

except Exception as e:
    print(f"An error occurred: {e}")
    # Handle the error appropriately
