try:
    file = open("nonexistent_file.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:  # Catching any other exception
    print(f"An unexpected error occurred: {e}")
finally:
    file.close() # Always execute regardless of exceptions.