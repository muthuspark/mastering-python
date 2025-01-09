import io

buffer_size = 4096  # Adjust as needed

with open("large_file.txt", "r") as f:
    while True:
        chunk = f.read(buffer_size)
        if not chunk:
            break
        # Process the chunk
        print(f"Processing chunk: {len(chunk)} bytes")

#Using io.BufferedIOBase for more control over buffering
with open("large_file.txt", "r") as f:
    buffered_file = io.BufferedReader(f)
    #process buffered_file.read(buffer_size)