from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode='r'):
    try:
        f = open(filename, mode)
        yield f  # The yield keyword marks the point where the context is entered
    finally:
        f.close()

with file_manager('another_file.txt', 'w') as f:
    f.write("Hello from a function-based context manager!")
