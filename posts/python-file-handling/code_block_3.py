try:
    with open("image.jpg", "rb") as file:
        image_data = file.read()
        # Process image_data...
except FileNotFoundError:
    print("Image file not found.")