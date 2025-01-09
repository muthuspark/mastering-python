#Append to a file
with open("my_file.txt", "a") as f:
    f.write("\nThis line is appended.")

#Write in binary mode
with open("image.jpg", "rb") as f:
    image_data = f.read()
