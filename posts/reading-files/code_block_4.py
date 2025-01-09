try:
    with open("image.jpg", 'rb') as file:
        data = file.read() # Reads the entire file as bytes
        # Process binary data (e.g., save, manipulate)

except FileNotFoundError:
    print(f"Error: File 'image.jpg' not found.")