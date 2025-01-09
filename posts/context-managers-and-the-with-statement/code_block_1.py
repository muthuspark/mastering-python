try:
    f = open("my_file.txt", "w")
    f.write("Hello, world!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if f:
        f.close()