import mmap
import os

filename = "my_large_file.txt"  # Replace with your file

with open(filename, "wb") as f:
    f.write(b"A" * (1024 * 1024 * 10)) # 10MB file filled with 'A'

try:
    with open(filename, "r+b") as f:  # Open in read/write binary mode
        mm = mmap.mmap(f.fileno(), 0)  # Map the entire file

        # Access data like a byte array
        data = mm[:10]  # Read the first 10 bytes
        print(f"First 10 bytes: {data}")

        # Modify the file in memory
        mm[0:5] = b"Hello" # Modify the first 5 bytes

        mm.close()
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if os.path.exists(filename):
        os.remove(filename) # Clean up the test file
