def read_large_file(filename, chunk_size=1024):
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

for chunk in read_large_file("massive_file.txt"):
    #process chunk
    pass
